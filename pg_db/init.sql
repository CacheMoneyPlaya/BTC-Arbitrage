\c crypt_arb;

CREATE TABLE buy_side (
  id SERIAL,
  asset VARCHAR ( 50 ) NOT NULL,
  exchange VARCHAR ( 50 ) NOT NULL,
  price DOUBLE PRECISION NOT NULL,
  size  DOUBLE PRECISION NOT NULL,
  order_value DOUBLE PRECISION NOT NULL,
  timestamp timestamp default current_timestamp
);

CREATE TABLE sell_side (
  id SERIAL,
  asset VARCHAR ( 50 ) NOT NULL,
  exchange VARCHAR ( 50 ) NOT NULL,
  price DOUBLE PRECISION NOT NULL,
  size  DOUBLE PRECISION NOT NULL,
  order_value DOUBLE PRECISION NOT NULL,
  timestamp timestamp default current_timestamp
);
