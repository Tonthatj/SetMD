CREATE TABLE public.doctors
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

ALTER TABLE public.doctors
    OWNER to postgres;
    
CREATE TABLE public.patients
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

ALTER TABLE public.patients
    OWNER to postgres;
    
CREATE TABLE public.productioncompanies
(
    id serial,
    user_id integer,
    expiration_date date,
    w9_form bytea,
    office_location character varying(64) COLLATE pg_catalog."default"
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.productioncompanies
    OWNER to postgres;
    
CREATE TABLE public.productioncoordinators
(
    id serial,
    user_id integer,
    production_company_id integer
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.productioncoordinators
    OWNER to postgres;
    
CREATE TABLE public.services
(
    id serial,
    name character varying(64) COLLATE pg_catalog."default",
    price integer,
    duration integer,
    travel boolean,
    doctor_id integer
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.services
    OWNER to postgres;
    
CREATE TABLE public.setmedics
(
    id serial,
    user_id integer,
    production_company_id integer
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.setmedics
    OWNER to postgres;
    
CREATE TABLE public.users
(
    id serial,
    name character varying(64) COLLATE pg_catalog."default",
    email character varying(64) COLLATE pg_catalog."default",
    phone integer,
    type character varying(64) COLLATE pg_catalog."default",
    disabled boolean
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.users
    OWNER to postgres;
