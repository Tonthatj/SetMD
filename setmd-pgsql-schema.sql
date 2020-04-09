--CREATE USER setmd;
--CREATE SCHEMA setmd;
CREATE TABLE setmd.doctors
(
    id serial,
    user_id integer,
    office_location character varying(255) COLLATE pg_catalog."default",
    is_god boolean
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE setmd.doctors
    OWNER to setmd;
    
CREATE TABLE setmd.patients
(
    id serial,
    user_id integer,
    consent_form bytea,
    privacy_agreement bytea,
    emergency_contact_user_id_1 integer,
    emergency_contact_user_id_2 integer
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE setmd.patients
    OWNER to setmd;
    
CREATE TABLE setmd.productioncompanies
(
    id serial,
    user_id integer,
    expiration_date date,
    w9_form bytea,
    office_location character varying(255) COLLATE pg_catalog."default"
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE setmd.productioncompanies
    OWNER to setmd;
    
CREATE TABLE setmd.productioncoordinators
(
    id serial,
    user_id integer,
    production_company_id integer
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE setmd.productioncoordinators
    OWNER to setmd;
    
CREATE TABLE setmd.services
(
    id serial,
    name character varying(64) COLLATE pg_catalog."default",
    price bigint,
    duration bigint,
    travel boolean,
    doctor_id integer
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE setmd.services
    OWNER to setmd;
    
CREATE TABLE setmd.setmedics
(
    id serial,
    user_id integer,
    production_company_id integer
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE setmd.setmedics
    OWNER to setmd;
    
CREATE TABLE setmd.users
(
    id serial,
    name character varying(64) COLLATE pg_catalog."default",
    email character varying(64) COLLATE pg_catalog."default",
    phone bigint,
    role character varying(64) COLLATE pg_catalog."default",
    disabled boolean
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE setmd.users
    OWNER to setmd;
