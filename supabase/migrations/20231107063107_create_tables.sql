--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1 (Ubuntu 15.1-1.pgdg20.04+1)
-- Dumped by pg_dump version 15.4 (Ubuntu 15.4-2.pgdg20.04+1)

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
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: challenges; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.challenges (
    id character varying NOT NULL,
    is_answered boolean,
    user_id character varying
);


ALTER TABLE public.challenges OWNER TO postgres;

--
-- Name: challenges_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.challenges_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.challenges_id_seq OWNER TO postgres;

--
-- Name: challenges_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.challenges_id_seq OWNED BY public.challenges.id;


--
-- Name: moves; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.moves (
    id integer NOT NULL,
    name character varying,
    type_id integer,
    pp integer,
    description character varying
);


ALTER TABLE public.moves OWNER TO postgres;

--
-- Name: moves_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.moves_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.moves_id_seq OWNER TO postgres;

--
-- Name: moves_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.moves_id_seq OWNED BY public.moves.id;


--
-- Name: pokemons; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pokemons (
    id integer NOT NULL,
    name character varying,
    type_id_1 integer,
    type_id_2 integer,
    img_url character varying,
    shiny_img_url character varying
);


ALTER TABLE public.pokemons OWNER TO postgres;

--
-- Name: pokemons_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pokemons_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pokemons_id_seq OWNER TO postgres;

--
-- Name: pokemons_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pokemons_id_seq OWNED BY public.pokemons.id;


--
-- Name: pokemoves; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pokemoves (
    id integer NOT NULL,
    move_id integer,
    learn_probability double precision,
    can_learn boolean,
    pokemon_id integer
);


ALTER TABLE public.pokemoves OWNER TO postgres;

--
-- Name: pokemoves_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pokemoves_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pokemoves_id_seq OWNER TO postgres;

--
-- Name: pokemoves_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pokemoves_id_seq OWNED BY public.pokemoves.id;


--
-- Name: quiz answers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."quiz answers" (
    id integer NOT NULL,
    quiz_id integer,
    move_id integer
);


ALTER TABLE public."quiz answers" OWNER TO postgres;

--
-- Name: quiz answers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."quiz answers_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."quiz answers_id_seq" OWNER TO postgres;

--
-- Name: quiz answers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."quiz answers_id_seq" OWNED BY public."quiz answers".id;


--
-- Name: quiz choices; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."quiz choices" (
    id integer NOT NULL,
    quiz_id integer,
    move_id integer
);


ALTER TABLE public."quiz choices" OWNER TO postgres;

--
-- Name: quiz choices_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."quiz choices_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."quiz choices_id_seq" OWNER TO postgres;

--
-- Name: quiz choices_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."quiz choices_id_seq" OWNED BY public."quiz choices".id;


--
-- Name: quizzes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.quizzes (
    id integer NOT NULL,
    challenge_id character varying,
    pokemon_id integer
);


ALTER TABLE public.quizzes OWNER TO postgres;

--
-- Name: quizzes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.quizzes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.quizzes_id_seq OWNER TO postgres;

--
-- Name: quizzes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.quizzes_id_seq OWNED BY public.quizzes.id;


--
-- Name: types; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.types (
    id integer NOT NULL,
    name character varying
);


ALTER TABLE public.types OWNER TO postgres;

--
-- Name: types_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.types_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.types_id_seq OWNER TO postgres;

--
-- Name: types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.types_id_seq OWNED BY public.types.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id character varying NOT NULL,
    api_token character varying,
    refresh_token character varying
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: challenges id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.challenges ALTER COLUMN id SET DEFAULT nextval('public.challenges_id_seq'::regclass);


--
-- Name: moves id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.moves ALTER COLUMN id SET DEFAULT nextval('public.moves_id_seq'::regclass);


--
-- Name: pokemons id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pokemons ALTER COLUMN id SET DEFAULT nextval('public.pokemons_id_seq'::regclass);


--
-- Name: pokemoves id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pokemoves ALTER COLUMN id SET DEFAULT nextval('public.pokemoves_id_seq'::regclass);


--
-- Name: quiz answers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."quiz answers" ALTER COLUMN id SET DEFAULT nextval('public."quiz answers_id_seq"'::regclass);


--
-- Name: quiz choices id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."quiz choices" ALTER COLUMN id SET DEFAULT nextval('public."quiz choices_id_seq"'::regclass);


--
-- Name: quizzes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.quizzes ALTER COLUMN id SET DEFAULT nextval('public.quizzes_id_seq'::regclass);


--
-- Name: types id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.types ALTER COLUMN id SET DEFAULT nextval('public.types_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: challenges challenges_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.challenges
    ADD CONSTRAINT challenges_pkey PRIMARY KEY (id);


--
-- Name: moves moves_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.moves
    ADD CONSTRAINT moves_pkey PRIMARY KEY (id);


--
-- Name: pokemons pokemons_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pokemons
    ADD CONSTRAINT pokemons_pkey PRIMARY KEY (id);


--
-- Name: pokemoves pokemoves_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pokemoves
    ADD CONSTRAINT pokemoves_pkey PRIMARY KEY (id);


--
-- Name: quiz answers quiz answers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."quiz answers"
    ADD CONSTRAINT "quiz answers_pkey" PRIMARY KEY (id);


--
-- Name: quiz choices quiz choices_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."quiz choices"
    ADD CONSTRAINT "quiz choices_pkey" PRIMARY KEY (id);


--
-- Name: quizzes quizzes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.quizzes
    ADD CONSTRAINT quizzes_pkey PRIMARY KEY (id);


--
-- Name: types types_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.types
    ADD CONSTRAINT types_pkey PRIMARY KEY (id);


--
-- Name: users users_api_token_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_api_token_key UNIQUE (api_token);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users users_refresh_token_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_refresh_token_key UNIQUE (refresh_token);


--
-- Name: ix_challenges_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_challenges_id ON public.challenges USING btree (id);


--
-- Name: ix_moves_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_moves_id ON public.moves USING btree (id);


--
-- Name: ix_pokemons_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_pokemons_id ON public.pokemons USING btree (id);


--
-- Name: ix_pokemoves_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_pokemoves_id ON public.pokemoves USING btree (id);


--
-- Name: ix_quiz answers_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "ix_quiz answers_id" ON public."quiz answers" USING btree (id);


--
-- Name: ix_quiz choices_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "ix_quiz choices_id" ON public."quiz choices" USING btree (id);


--
-- Name: ix_quizzes_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_quizzes_id ON public.quizzes USING btree (id);


--
-- Name: ix_types_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_types_id ON public.types USING btree (id);


--
-- Name: ix_users_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_users_id ON public.users USING btree (id);


--
-- Name: challenges challenges_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.challenges
    ADD CONSTRAINT challenges_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: moves moves_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.moves
    ADD CONSTRAINT moves_type_id_fkey FOREIGN KEY (type_id) REFERENCES public.types(id);


--
-- Name: pokemons pokemons_type_id_1_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pokemons
    ADD CONSTRAINT pokemons_type_id_1_fkey FOREIGN KEY (type_id_1) REFERENCES public.types(id);


--
-- Name: pokemons pokemons_type_id_2_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pokemons
    ADD CONSTRAINT pokemons_type_id_2_fkey FOREIGN KEY (type_id_2) REFERENCES public.types(id);


--
-- Name: pokemoves pokemoves_move_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pokemoves
    ADD CONSTRAINT pokemoves_move_id_fkey FOREIGN KEY (move_id) REFERENCES public.moves(id);


--
-- Name: pokemoves pokemoves_pokemon_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pokemoves
    ADD CONSTRAINT pokemoves_pokemon_id_fkey FOREIGN KEY (pokemon_id) REFERENCES public.pokemons(id);


--
-- Name: quiz answers quiz answers_move_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."quiz answers"
    ADD CONSTRAINT "quiz answers_move_id_fkey" FOREIGN KEY (move_id) REFERENCES public.moves(id);


--
-- Name: quiz answers quiz answers_quiz_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."quiz answers"
    ADD CONSTRAINT "quiz answers_quiz_id_fkey" FOREIGN KEY (quiz_id) REFERENCES public.quizzes(id);


--
-- Name: quiz choices quiz choices_move_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."quiz choices"
    ADD CONSTRAINT "quiz choices_move_id_fkey" FOREIGN KEY (move_id) REFERENCES public.moves(id);


--
-- Name: quiz choices quiz choices_quiz_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."quiz choices"
    ADD CONSTRAINT "quiz choices_quiz_id_fkey" FOREIGN KEY (quiz_id) REFERENCES public.quizzes(id);


--
-- Name: quizzes quizzes_challenge_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.quizzes
    ADD CONSTRAINT quizzes_challenge_id_fkey FOREIGN KEY (challenge_id) REFERENCES public.challenges(id);


--
-- Name: quizzes quizzes_pokemon_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.quizzes
    ADD CONSTRAINT quizzes_pokemon_id_fkey FOREIGN KEY (pokemon_id) REFERENCES public.pokemons(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: pg_database_owner
--

GRANT USAGE ON SCHEMA public TO postgres;
GRANT USAGE ON SCHEMA public TO anon;
GRANT USAGE ON SCHEMA public TO authenticated;
GRANT USAGE ON SCHEMA public TO service_role;


--
-- Name: TABLE alembic_version; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.alembic_version TO anon;
GRANT ALL ON TABLE public.alembic_version TO authenticated;
GRANT ALL ON TABLE public.alembic_version TO service_role;


--
-- Name: TABLE challenges; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.challenges TO anon;
GRANT ALL ON TABLE public.challenges TO authenticated;
GRANT ALL ON TABLE public.challenges TO service_role;


--
-- Name: SEQUENCE challenges_id_seq; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON SEQUENCE public.challenges_id_seq TO anon;
GRANT ALL ON SEQUENCE public.challenges_id_seq TO authenticated;
GRANT ALL ON SEQUENCE public.challenges_id_seq TO service_role;


--
-- Name: TABLE moves; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.moves TO anon;
GRANT ALL ON TABLE public.moves TO authenticated;
GRANT ALL ON TABLE public.moves TO service_role;


--
-- Name: SEQUENCE moves_id_seq; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON SEQUENCE public.moves_id_seq TO anon;
GRANT ALL ON SEQUENCE public.moves_id_seq TO authenticated;
GRANT ALL ON SEQUENCE public.moves_id_seq TO service_role;


--
-- Name: TABLE pokemons; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.pokemons TO anon;
GRANT ALL ON TABLE public.pokemons TO authenticated;
GRANT ALL ON TABLE public.pokemons TO service_role;


--
-- Name: SEQUENCE pokemons_id_seq; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON SEQUENCE public.pokemons_id_seq TO anon;
GRANT ALL ON SEQUENCE public.pokemons_id_seq TO authenticated;
GRANT ALL ON SEQUENCE public.pokemons_id_seq TO service_role;


--
-- Name: TABLE pokemoves; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.pokemoves TO anon;
GRANT ALL ON TABLE public.pokemoves TO authenticated;
GRANT ALL ON TABLE public.pokemoves TO service_role;


--
-- Name: SEQUENCE pokemoves_id_seq; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON SEQUENCE public.pokemoves_id_seq TO anon;
GRANT ALL ON SEQUENCE public.pokemoves_id_seq TO authenticated;
GRANT ALL ON SEQUENCE public.pokemoves_id_seq TO service_role;


--
-- Name: TABLE "quiz answers"; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public."quiz answers" TO anon;
GRANT ALL ON TABLE public."quiz answers" TO authenticated;
GRANT ALL ON TABLE public."quiz answers" TO service_role;


--
-- Name: SEQUENCE "quiz answers_id_seq"; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON SEQUENCE public."quiz answers_id_seq" TO anon;
GRANT ALL ON SEQUENCE public."quiz answers_id_seq" TO authenticated;
GRANT ALL ON SEQUENCE public."quiz answers_id_seq" TO service_role;


--
-- Name: TABLE "quiz choices"; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public."quiz choices" TO anon;
GRANT ALL ON TABLE public."quiz choices" TO authenticated;
GRANT ALL ON TABLE public."quiz choices" TO service_role;


--
-- Name: SEQUENCE "quiz choices_id_seq"; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON SEQUENCE public."quiz choices_id_seq" TO anon;
GRANT ALL ON SEQUENCE public."quiz choices_id_seq" TO authenticated;
GRANT ALL ON SEQUENCE public."quiz choices_id_seq" TO service_role;


--
-- Name: TABLE quizzes; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.quizzes TO anon;
GRANT ALL ON TABLE public.quizzes TO authenticated;
GRANT ALL ON TABLE public.quizzes TO service_role;


--
-- Name: SEQUENCE quizzes_id_seq; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON SEQUENCE public.quizzes_id_seq TO anon;
GRANT ALL ON SEQUENCE public.quizzes_id_seq TO authenticated;
GRANT ALL ON SEQUENCE public.quizzes_id_seq TO service_role;


--
-- Name: TABLE types; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.types TO anon;
GRANT ALL ON TABLE public.types TO authenticated;
GRANT ALL ON TABLE public.types TO service_role;


--
-- Name: SEQUENCE types_id_seq; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON SEQUENCE public.types_id_seq TO anon;
GRANT ALL ON SEQUENCE public.types_id_seq TO authenticated;
GRANT ALL ON SEQUENCE public.types_id_seq TO service_role;


--
-- Name: TABLE users; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.users TO anon;
GRANT ALL ON TABLE public.users TO authenticated;
GRANT ALL ON TABLE public.users TO service_role;


--
-- Name: SEQUENCE users_id_seq; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON SEQUENCE public.users_id_seq TO anon;
GRANT ALL ON SEQUENCE public.users_id_seq TO authenticated;
GRANT ALL ON SEQUENCE public.users_id_seq TO service_role;


--
-- Name: DEFAULT PRIVILEGES FOR SEQUENCES; Type: DEFAULT ACL; Schema: public; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON SEQUENCES  TO postgres;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON SEQUENCES  TO anon;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON SEQUENCES  TO authenticated;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON SEQUENCES  TO service_role;


--
-- Name: DEFAULT PRIVILEGES FOR SEQUENCES; Type: DEFAULT ACL; Schema: public; Owner: supabase_admin
--

ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON SEQUENCES  TO postgres;
ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON SEQUENCES  TO anon;
ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON SEQUENCES  TO authenticated;
ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON SEQUENCES  TO service_role;


--
-- Name: DEFAULT PRIVILEGES FOR FUNCTIONS; Type: DEFAULT ACL; Schema: public; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON FUNCTIONS  TO postgres;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON FUNCTIONS  TO anon;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON FUNCTIONS  TO authenticated;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON FUNCTIONS  TO service_role;


--
-- Name: DEFAULT PRIVILEGES FOR FUNCTIONS; Type: DEFAULT ACL; Schema: public; Owner: supabase_admin
--

ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON FUNCTIONS  TO postgres;
ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON FUNCTIONS  TO anon;
ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON FUNCTIONS  TO authenticated;
ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON FUNCTIONS  TO service_role;


--
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: public; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON TABLES  TO postgres;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON TABLES  TO anon;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON TABLES  TO authenticated;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON TABLES  TO service_role;


--
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: public; Owner: supabase_admin
--

ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON TABLES  TO postgres;
ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON TABLES  TO anon;
ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON TABLES  TO authenticated;
ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON TABLES  TO service_role;


--
-- PostgreSQL database dump complete
--

