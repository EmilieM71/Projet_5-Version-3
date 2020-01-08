CREATE DATABASE PurBeurre CHARACTER SET 'utf8mb4';
USE PurBeurre;

-- creating the table `category`
CREATE TABLE category (
                id_cat INTEGER AUTO_INCREMENT NOT NULL,
                name_cat VARCHAR(255) NOT NULL,
                CONSTRAINT category_pk PRIMARY KEY (id_cat)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE UNIQUE INDEX category_idx
 ON category ( name_cat );

-- creating the table `store`
CREATE TABLE store (
                id_store INTEGER AUTO_INCREMENT NOT NULL,
                name_store VARCHAR(255) NOT NULL,
                CONSTRAINT store_pk PRIMARY KEY (id_store)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE UNIQUE INDEX store_idx
 ON store ( name_store );

-- creating the table `brand`
CREATE TABLE brand (
                id_brand INTEGER AUTO_INCREMENT NOT NULL,
                name_brand VARCHAR(255) NOT NULL,
                CONSTRAINT brand_pk PRIMARY KEY (id_brand)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE UNIQUE INDEX brand_idx
 ON brand ( name_brand );

-- creating the table `food`
CREATE TABLE food (
                id_food VARCHAR(20) NOT NULL,
                name_food VARCHAR(500) NOT NULL,
                nutriscore VARCHAR(1) NOT NULL,
                url VARCHAR(255),
                ingredient VARCHAR(5000),
                palm_oil VARCHAR(100),
                allergen VARCHAR(1000),
                energy_100g VARCHAR(10),
                energy VARCHAR(10),
                fat_100g VARCHAR(10),
                saturated_fat_100g VARCHAR(10),
                carbohydrates_100g VARCHAR(10),
                sugars_100g VARCHAR(10),
                proteins_100g VARCHAR(10),
                salt_100g VARCHAR(100),
                sodium_100g VARCHAR(100),
                nutrition_score_fr_100g SMALLINT,
                nova_group_100g SMALLINT,
                CONSTRAINT food_pk PRIMARY KEY (id_food)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- creating the table `users`
CREATE TABLE user (
                id_user INTEGER AUTO_INCREMENT NOT NULL,
                pseudo VARCHAR(255) NOT NULL,
                e_mail VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                CONSTRAINT user_pk PRIMARY KEY (id_user)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE UNIQUE INDEX user_idx
 ON user ( pseudo );

-- creating the table `food_brand`
CREATE TABLE food_brand (
                brand_id INTEGER NOT NULL,
                food_id VARCHAR(20) NOT NULL,
                CONSTRAINT food_brand_pk PRIMARY KEY (brand_id, food_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- creating the table `food_store`
CREATE TABLE food_store (
                store_id INTEGER NOT NULL,
                food_id VARCHAR(20) NOT NULL,
                CONSTRAINT food_store_pk PRIMARY KEY (store_id, food_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- creating the table `category_food`
CREATE TABLE category_food (
                category_id INTEGER NOT NULL,
                food_id VARCHAR(20) NOT NULL,
                CONSTRAINT category_food_pk PRIMARY KEY (category_id, food_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- creating the table `user_food`
CREATE TABLE user_food_substitute (
                food_id VARCHAR(20) NOT NULL,
                substitute_id VARCHAR(20) NOT NULL,
                user_id INTEGER NOT NULL,
                CONSTRAINT user_food_substitute_pk PRIMARY KEY (food_id, substitute_id, user_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE food_brand ADD CONSTRAINT brand_food_brand_fk
FOREIGN KEY (brand_id)
REFERENCES brand (id_brand)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE food_store ADD CONSTRAINT store_food_store_fk
FOREIGN KEY (store_id)
REFERENCES store (id_store)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE food_store ADD CONSTRAINT food_food_store_fk
FOREIGN KEY (food_id)
REFERENCES food (id_food)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE user_food_substitute ADD CONSTRAINT food_user_food_substitute_fk
FOREIGN KEY (food_id)
REFERENCES food (id_food)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE user_food_substitute ADD CONSTRAINT food_user_food_substitute_fk1
FOREIGN KEY (substitute_id)
REFERENCES food (id_food)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE user_food_substitute ADD CONSTRAINT user_user_food_substitute_fk
FOREIGN KEY (user_id)
REFERENCES user (id_user)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE category_food ADD CONSTRAINT food_category_food_fk
FOREIGN KEY (food_id)
REFERENCES food (id_food)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE category_food ADD CONSTRAINT category_category_food_fk
FOREIGN KEY (category_id)
REFERENCES category (id_cat)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE food_brand ADD CONSTRAINT food_food_brand_fk
FOREIGN KEY (food_id)
REFERENCES food (id_food)
ON DELETE NO ACTION
ON UPDATE NO ACTION;