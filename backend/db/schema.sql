CREATE SCHEMA IF NOT EXISTS recipe_app;

CREATE TABLE recipe_app.foods (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    preparation_time INT,
    calorie INT,
    category VARCHAR(10), --  breakfast, lunch, dinner
    is_favorite BOOLEAN DEFAULT FALSE,
    rating FLOAT,
    total_reviews INT,
    photo_url VARCHAR(255)
);

CREATE TABLE recipe_app.ingredients (
    id SERIAL PRIMARY KEY,
    food_id INT REFERENCES recipe_app.foods(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    quantity VARCHAR(50) NOT NULL,
    photo_url VARCHAR(255)
);

