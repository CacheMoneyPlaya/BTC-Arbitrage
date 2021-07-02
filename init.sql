\c crypt_arb;

CREATE TABLE price_points (
   exchange VARCHAR ( 50 ) NOT NULL,
   ask INTEGER NOT NULL,
   bid INTEGER NOT NULL,
   timestamp timestamp default current_timestamp
);
