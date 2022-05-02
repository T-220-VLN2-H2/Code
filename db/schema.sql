-- T-220-VLN2 - Group 2
--
-- Schema for FireSale!
--
-- Helgi Hákonarson <helgihak20@ru.is>
-- Konráð Elí Sigurgeirsson <konrad21@ru.is>
-- Patrekur Þór Agnarsson <patrekur20@ru.is>
-- Sigurður Baldvin Friðriksson <sigurdurf21@ru.is>

-- TODO: create schema

-- drop table if exists  cascade;

drop table if exists users cascade;

create table users (
  id serial primary key,
  full_name varchar not null,
  user_name varchar not null,
  email varchar not null,
  password_hash varchar not null
);

drop table if exists notifications cascade;
create table notifications (
  id serial primary key,
  title varchar not null,
  message varchar not null,
  time timestamp
);

drop table if exists search_history cascade;
create table search_history (
  search_string varchar,
  time timestamp
  -- TODO: add pk (search_string, time)
);

drop table if exists items cascade;
create table items (
  id serial primary key,
  price deciamal, -- null if auction
  condition

);
