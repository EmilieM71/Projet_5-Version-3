CREATE DATABASE PurBeurre CHARACTER SET 'utf8';
USE PurBeurre;

-- creating the table `category`
CREATE TABLE category (
                id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(255) NOT NULL UNIQUE,
                PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- creating the table `store`
CREATE TABLE store (
                id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(255) NOT NULL UNIQUE,
                PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- creating the table `brand`
CREATE TABLE brand (
                id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(255) NOT NULL,
                PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- creating the table `food`
CREATE TABLE food (
                id VARCHAR(20) NOT NULL,
                name VARCHAR(500) NOT NULL,
                nutriscore VARCHAR(1),
                url VARCHAR(255),
                ingredient VARCHAR(1000),
                palm_oil VARCHAR(20),
                allergen VARCHAR(1000),
                energy_100g VARCHAR(10),
                energy VARCHAR(10),
                fat_100g VARCHAR(10),
                saturated_fat_100g VARCHAR(10),
                carbohydrates_100g VARCHAR(10),
                sugars_100g VARCHAR(10),
                proteins_100g VARCHAR(10),
                salt_100g VARCHAR(10),
                sodium_100g VARCHAR(10),
                nutrition_score_fr_100g INT,
                nova_group_100g INT,
                PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- creating the table `users`
CREATE TABLE user (
                id INT AUTO_INCREMENT NOT NULL,
                e_mail VARCHAR(255) NOT NULL,
                pseudo VARCHAR(255) NOT NULL,
                password VARCHAR(20) NOT NULL,
                PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE UNIQUE INDEX user_idx
 ON user
 ( password, pseudo );

-- creating the table `food_brand`
CREATE TABLE food_brand (
                id_food VARCHAR(20) NOT NULL,
                id_brand INT NOT NULL,
                PRIMARY KEY (id_food, id_brand)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- creating the table `food_store`
CREATE TABLE food_store (
                id_food VARCHAR(20) NOT NULL,
                id_store INT NOT NULL,
                PRIMARY KEY (id_food, id_store)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- creating the table `category_food`
CREATE TABLE category_food (
                id_category INT NOT NULL,
                id_food VARCHAR(20) NOT NULL,
                PRIMARY KEY (id_category, id_food)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- creating the table `user_food`
CREATE TABLE user_food_substitute (
                id_user INT NOT NULL,
                id_food VARCHAR(20) NOT NULL,
                id_substitute VARCHAR(20) NOT NULL,
                PRIMARY KEY (id_user, id_food, id_substitute)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE food_brand ADD CONSTRAINT brands_food_brands_fk
FOREIGN KEY (id_brand)
REFERENCES brand (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE food_store ADD CONSTRAINT store_food_store_fk
FOREIGN KEY (id_store)
REFERENCES store (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE food_store ADD CONSTRAINT food_food_store_fk
FOREIGN KEY (id_food)
REFERENCES food (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE user_food_substitute ADD CONSTRAINT food_user_food_fk
FOREIGN KEY (id_food)
REFERENCES food (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE user_food_substitute ADD CONSTRAINT food_user_food_fk1
FOREIGN KEY (id_substitute)
REFERENCES food (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE user_food_substitute ADD CONSTRAINT user_user_food_fk
FOREIGN KEY (id_user)
REFERENCES user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE category_food ADD CONSTRAINT food_category_food_fk
FOREIGN KEY (id_food)
REFERENCES food (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE food_brand ADD CONSTRAINT food_food_brands_fk
FOREIGN KEY (id_food)
REFERENCES food (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE category_food ADD CONSTRAINT category_category_food_fk
FOREIGN KEY (id_category)
REFERENCES category (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;