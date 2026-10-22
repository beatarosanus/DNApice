CREATE DATABASE DNAPICE;
USE DNAPICE;

CREATE TABLE Bioma (
    id_bioma INT PRIMARY KEY,
    flora VARCHAR(100),
    clima VARCHAR(100),
    fauna VARCHAR(100),
    nome VARCHAR(100),
    umidade FLOAT,
    temperatura FLOAT
);

CREATE TABLE Corpo_Humano (
    id_corpo INT PRIMARY KEY,
    ph FLOAT,
    saturacao_de_oxigenio FLOAT,
    pressao_arterial VARCHAR(20),
    nome VARCHAR(100),
    hidratacao FLOAT,
    temperatura_corpo FLOAT,
    bioma_atual INT,
    FOREIGN KEY (bioma_atual) REFERENCES Bioma(id_bioma)
);

CREATE TABLE Pulmao (
    id_pulmao INT PRIMARY KEY,
    estado_saude VARCHAR(100),
    id_corpo INT UNIQUE,
    FOREIGN KEY (id_corpo) REFERENCES Corpo_Humano(id_corpo)
);

CREATE TABLE Rins (
    id_rins INT PRIMARY KEY,
    filtracao FLOAT,
    id_corpo INT UNIQUE,
    FOREIGN KEY (id_corpo) REFERENCES Corpo_Humano(id_corpo)
);

CREATE TABLE Sistema_Excretor (
    id_sistema_excretor INT PRIMARY KEY,
    capacidade_maxima_urina FLOAT,
    id_corpo INT UNIQUE,
    FOREIGN KEY (id_corpo) REFERENCES Corpo_Humano(id_corpo)
);

CREATE TABLE Deserto (
    id_bioma INT PRIMARY KEY,
    temperatura_dia FLOAT,
    temperatura_noite FLOAT,
    FOREIGN KEY (id_bioma) REFERENCES Bioma(id_bioma)
);

CREATE TABLE Taiga (
    id_bioma INT PRIMARY KEY,
    FOREIGN KEY (id_bioma) REFERENCES Bioma(id_bioma)
);

CREATE TABLE Tundra (
    id_bioma INT PRIMARY KEY,
    altitude_metros FLOAT,
    velocidade_vento FLOAT,
    FOREIGN KEY (id_bioma) REFERENCES Bioma(id_bioma)
);
--Cadastro dos biomas:
INSERT INTO Bioma (id_bioma, flora, clima, fauna, nome, umidade, temperatura)
VALUES
(1, 'Cactos e arbustos', 'Arido', 'Repteis e roedores', 'Deserto', 15, 40),
(2, 'Coniferas', 'Frio e subartico', 'Alces e ursos', 'Taiga', 60, -10),
(3, 'Musgos e liquens', 'Polar', 'Renas e raposas-do-artico', 'Tundra', 40, -20);

INSERT INTO Deserto (id_bioma, temperatura_dia, temperatura_noite) VALUES (1, 40, 20);

INSERT INTO Taiga (id_bioma) VALUES (2);

INSERT INTO Tundra (id_bioma, altitude_metros, velocidade_vento) VALUES (3, 500, 30);
INSERT INTO Corpo_Humano (id_corpo, ph, saturacao_de_oxigenio, pressao_arterial, nome, hidratacao, temperatura_corpo, bioma_atual)
VALUES (1, 7.35, 98.0, '120/80', 'Matheus', 60.0, 36.5, 1);

INSERT INTO Pulmao (id_pulmao, estado_saude, id_corpo) VALUES (1, 'Saudavel', 1);

INSERT INTO Rins (id_rins, filtracao, id_corpo) VALUES (1, 120.0, 1);

INSERT INTO Sistema_Excretor (id_sistema_excretor, capacidade_maxima_urina, id_corpo) VALUES (1, 500.0, 1);
-- Cadastro dos organismos:
INSERT INTO Corpo_Humano (id_corpo, ph, saturacao_de_oxigenio, pressao_arterial, nome, hidratacao, temperatura_corpo, bioma_atual)
VALUES (2, 7.40, 99.0, '110/70', 'Beatriz', 65.0, 36.8, 2);

INSERT INTO Pulmao (id_pulmao, estado_saude, id_corpo) VALUES (2, 'Saudavel', 2);

INSERT INTO Rins (id_rins, filtracao, id_corpo) VALUES (2, 115.0, 2);

INSERT INTO Sistema_Excretor (id_sistema_excretor, capacidade_maxima_urina, id_corpo) VALUES (2, 450.0, 2);
