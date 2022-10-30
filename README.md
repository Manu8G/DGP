# DGP

## **Instrucciones para usar la base de datos**

* Construir docker 
```
	docker compose build
```

* Iniciar servidor 
```
	docker compose up
```

* Hacer migraciones de las tablas (creo que lo tenemos que hacer todos al principio)   
```
docker compose run web python manage.py makemigrations    
docker compose run web python manage.py migrate   
```

* Crear super usuario (En teoría lo he hecho yo, pero igual que antes no se si se ha guardado)
```
docker compose run web python manage.py createsuperuser
```
