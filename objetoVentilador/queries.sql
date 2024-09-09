CREATE TABLE `ventilador` (
id ventilador PRIMARY KEY,
velocidades varchar(20),
estados varchar(50),
id_velocidad fk,
id_estado fk
);

CREATE TABLE `velocidades` (
id velocidad PRIMARY KEY,
potencia varchar(100),
consumo_energia varchar(50),
rpm int
);

CREATE TABLE `estados` (
id estado PRIMARY KEY,
descripcion varchar(200)
);

ALTER TABLE `velocidades` ADD FOREIGN KEY (`id`) REFERENCES `ventilador` (`id`);

ALTER TABLE `estados` ADD FOREIGN KEY (`id`) REFERENCES `ventilador` (`id`);



""" Sentencias INSERT """
INSERT INTO velocidades (potencia, consumo_energia, rpm) VALUES ('0 W', '1 hora', 700);
INSERT INTO velocidades (potencia, consumo_energia, rpm) VALUES ('20 W', '1 hora', 700);
INSERT INTO velocidades (potencia, consumo_energia, rpm) VALUES ('35 W', '1 hora', 1100);
INSERT INTO velocidades (potencia, consumo_energia, rpm) VALUES ('75 W', '1 hora', 1750);
INSERT INTO estados (descripcion) VALUES ('El ventilador se encuentra apagado');
INSERT INTO estados (descripcion) VALUES ('El ventilador se encendio y esta funcionando a una velocidad baja');
INSERT INTO estados (descripcion) VALUES ('Velocidad Media');
INSERT INTO estados (descripcion) VALUES ('Velocidad Alta');
INSERT INTO ventilador (velocidades_id, estados_id) VALUES (1, 1);
INSERT INTO ventilador (velocidades_id, estados_id) VALUES (2, 2); 
INSERT INTO ventilador (velocidades_id, estados_id) VALUES (3, 3);


""" Sentencias SELECT """

SELECT estados.descripcion
FROM ventilador
JOIN estados ON ventilador.estados_id = estados.id;

SELECT id, potencia, consumo_energia, rpm
FROM velocidades
WHERE potencia = '0 W' AND consumo_energia = '1 hora' AND rpm = 700;

SELECT COUNT(*) AS total_velocidades
FROM velocidades

SELECT COUNT(DISTINCT ventilador.estados_id) AS total_estados
FROM ventilador

SELECT COUNT(*) AS cantidad
FROM estados
WHERE descripcion = 'Velocidad Media'



