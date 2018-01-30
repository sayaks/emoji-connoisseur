#!/usr/bin/env python3
# encoding: utf-8

import asyncio
from pathlib import Path
import json

import asyncpg


def _get_config():
	with open(DATA_DIR/'config.json') as config_file:
		config = json.load(config_file)
	return config


async def _get_db():
	credentials = {
		'user': 'connoisseur',
		'password': CONFIG['database']['password'],
		'database': 'connoisseur',
		'host': '127.0.0.1'}
	db = await asyncpg.create_pool(**credentials)
	await db.execute('CREATE SCHEMA IF NOT EXISTS connoisseur')
	await db.execute(
		'CREATE TABLE IF NOT EXISTS connoisseur.emojis('
			'name VARCHAR(32) NOT NULL,'
			'id BIGINT NOT NULL,'
			'author BIGINT NOT NULL)')
	await db.execute('CREATE TABLE IF NOT EXISTS connoisseur.blacklists(id bigint NOT NULL)')
	return db


DATA_DIR = Path('data')
CONFIG = _get_config()
DB = asyncio.get_event_loop().run_until_complete(_get_db())