#!/usr/bin/env python3
import datetime
import psycopg2

DBname = "news"


def get_titles():

    db = psycopg2.connect(dbname=DBname)
    c = db.cursor()
    query = """

            select a.title, count(a.slug)
            as views from articles a, log l where l.path
            like '/article/'||a.slug
            group by a.title
            order by views desc limit 3;

            """

    c.execute(query)
    titles = c.fetchall()
    db.close()

    return titles


def get_authors():

    db = psycopg2.connect(dbname=DBname)
    c = db.cursor()
    query = """

            select ath.name, count(a.slug)
            as views from articles a,authors ath, log l
            where a.author = ath.id and l.path like '/article/'||a.slug
            group by ath.name order by Views desc;

            """

    c.execute(query)
    authors = c.fetchall()
    db.close()

    return authors


def get_errors():

    db = psycopg2.connect(dbname=DBname)
    c = db.cursor()
    query = """
            select e.errorDate,
            Round((cast(e.attemp as float) / cast(t.attemp as float) * 100)
            ::numeric,2) as percentage from ErrorAttemp e , TotalAttemp t where
            e.errorDate = t.attempdate and Round((cast(e.attemp as float) /
            cast(t.attemp as float) * 100)::numeric,2) > 1;

            """

    c.execute(query)
    errors = c.fetchall()
    db.close()

    return errors
