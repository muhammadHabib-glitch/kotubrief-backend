# import json
# import pyodbc
# from datetime import datetime
#
# # 1. Load JSON file
# with open("
#
#
# gutenberg_books.json", "r", encoding="utf-8") as f:
#     books_data = json.load(f)
#
# # 2. Connect to SQL Server
# conn = pyodbc.connect(
#     "Driver={ODBC Driver 17 for SQL Server};"
#     "Server=DESKTOP-8TUN3M3\SQLEXPRESS;"   # e.g. DESKTOP-8UN3NM3\SQLEXPRESS
#     "Database=KotuBrief;"
#     "Trusted_Connection=yes;"
# )
# cursor = conn.cursor()
#
# # 3. Insert data (user_id = NULL for Gutenberg imports)
# for book in books_data:
#     title = book.get("Book Name")
#     author = book.get("Author Name")
#     cover_image_url = book.get("Image URL")
#     main_category = book.get("Category")
#     sub_category = book.get("Sub Category")
#     user_id = None  # Gutenberg books don't belong to a specific user
#
#     cursor.execute("""
#         INSERT INTO Books (user_id, title, author, cover_image_url, main_category, sub_category, created_at)
#         VALUES (?, ?, ?, ?, ?, ?, ?)
#     """, (user_id, title, author, cover_image_url, main_category, sub_category, datetime.now()))
#
# # 4. Commit & close
# conn.commit()
# cursor.close()
# conn.close()
#
# print("✅ All Gutenberg books inserted successfully!")
