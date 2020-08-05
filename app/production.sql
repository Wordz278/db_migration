--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.17
-- Dumped by pg_dump version 10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO "user";

--
-- Name: recruits; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.recruits (
    first_name character varying(100),
    surname character varying(100),
    github_name character varying(100),
    id_number bigint,
    personal_email_address character varying(100),
    cohort character varying(100),
    rocketchat_user character varying(100)
);


ALTER TABLE public.recruits OWNER TO "user";

--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.alembic_version (version_num) FROM stdin;
6288520e4b21
\.


--
-- Data for Name: recruits; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.recruits (first_name, surname, github_name, id_number, personal_email_address, cohort, rocketchat_user) FROM stdin;
Jacky	Sledge	JackyS92	9612075607900	JSledge@gmail.com	\N	\N
Lucky	Black	LuckyBlack009!	9612075607900	LuckyBlue@gmail.com	\N	\N
Oslo	King	OS92	9612075607950	OD92@gmail.com	C26_JAVA	\N
Jane	Doe	JaneDoe009!	9612075607900	JDoe@gmail.com	C26_JAVA	\N
Floyd	Money	MoneyFloyd	9212075607900	FM1000@gmail.com	C26_JAVA	\N
Woody	Green	WoodyG009!	9612075607900	WG@gmail.com	C26_JAVA	\N
Tumelo	Khoza	TK009!	9112075607700	TK@gmail.com	C26_JAVA	\N
Julia	Cage	JCage92	9412075657950	JCage@gmail.com	C27_Web_Dev	JCage92
Timu	Grey	TimuGrey009!	9612075607901	TGrey@gmail.com	C27_Web_Dev	TimuGrey009!
Fortunate	Blue	MoneyFloyd	9212075607902	FBlue1000@gmail.com	C27_Web_Dev	FBlue1000
Micky	Black	MickyB009!	9412075607903	MK@gmail.com	C27_Web_Dev	MK009!
Zoe	Yellow	ZoeYel09	9212075607704	ZY@gmail.com	C27_Web_Dev	ZoeY
Jake	Rod	JRod92	9412075657951	JRod@gmail.com	C28_Data_Scientists	JRod92
Charly	Pop	CPop009!	9512075607909	CPop@gmail.com	C28_Data_Scientists	CPop009!
Allan	Brown	ABrown	9212075607903	ABrown1000@gmail.com	C28_Data_Scientists	ABrown1000
Sam	Husk	SamH009!	9312073687909	SamH@gmail.com	C28_Data_Scientists	SamH009!
Joe	Campbell	JoeCl09	9512075607705	JoeC@gmail.com	C28_Data_Scientists	JoeC
\.


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: recruits recruits_personal_email_address_key; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.recruits
    ADD CONSTRAINT recruits_personal_email_address_key UNIQUE (personal_email_address);


--
-- PostgreSQL database dump complete
--

