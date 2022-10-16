# DGP

## **Instrucciones para usar la base de datos**

* Descargar el docker:   
```
	docker pull luistf24/dgp_tecnogurus:1.0
```

* Ejecutar el docker:
```
	docker compose up
```

* Entrar en la base de datos (la contraseña está en el grupo de telegram):
```
	docker compose exec mysql mysql -p
```

* Seleccionar la base de datos (db es el nombre de la base de datos):
```
	use db
```

* Ver que están las tablas:
```
	show tables;
```
