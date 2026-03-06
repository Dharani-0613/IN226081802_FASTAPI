from fastapi import FastAPI
app = FastAPI()

products = [
    {"id": 1, "name": "Wireless Mouse", "price": 499, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 89, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "USB Hub", "price": 799, "category": "Electronics", "in_stock": False},
    {"id": 4, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True},
    #Task 1 — Add these 3 new products:
    {"id": 5, "name": "Laptop Stand", "price": 999, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1299, "category": "Electronics", "in_stock": False},
]

#Q1 - All produxts:
@app.get("/products")
def get_products():
    return {"products": products, "total": len(products)}

#Q2 - Filtering by category:
@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):
    filtered = [p for p in products if p["category"].lower() == category_name.lower()]
    if not filtered:
        return {"error": "No products found in this category"}
    return filtered

#Q3 - In stock:
@app.get("/products/instock")
def get_instock():
    available = [p for p in products if p["in_stock"] == True]
    return {"in_stock_products": available, "count": len(available)}

#Q4 - Store Summary
@app.get("/store/summary")
def store_summary():
    in_stock = [p for p in products if p["in_stock"]]
    categories = list(set(p["category"] for p in products))
    return {
        "store_name": "My E-commerce Store",
        "total_products": len(products),
        "in_stock": len(in_stock),
        "out_of_stock": len(products) - len(in_stock),
        "categories": categories
    }

#Q5 - Searching by keyword
@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    matched = [p for p in products if keyword.lower() in p["name"].lower()]
    if not matched:
        return {"message": "No products matched your search"}
    return {"matched_products": matched, "count": len(matched)}

#Bonus Question: 
@app.get("/products/deals")
def get_deals():
    cheapest = min(products, key=lambda p: p["price"])
    expensive = max(products, key=lambda p: p["price"])
    return {"best_deal": cheapest, "premium_pick": expensive}
