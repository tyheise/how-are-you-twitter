up:
	docker-compose up

down:
	docker-compose down

django-sh:
	docker exec -it how-are-you-twitter_django_1 /bin/bash

commit-django:
	docker commit how-are-you-twitter_django_1 how-are-you-twitter_django
