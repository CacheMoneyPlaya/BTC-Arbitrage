\c crypt_arb;

CREATE TABLE price_points (
   asset VARCHAR ( 50 ) NOT NULL,
   exchange VARCHAR ( 50 ) NOT NULL,
   side VARCHAR ( 50 ) NOT NULL,
   price REAL NOT NULL,
   size REAL NOT NULL,
   timestamp timestamp default current_timestamp
);
