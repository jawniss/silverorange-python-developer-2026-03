dev:
	make -j2 runserver assets

runserver:
	uv run python manage.py runserver

assets:
	npm run dev
