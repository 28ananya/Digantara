import os
from app import create_app, db

app = create_app()

# Ensure tables are created at startup
with app.app_context():
    db.create_all()
    print("Database tables created successfully!")

# Use the Render-assigned port
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
