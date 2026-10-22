CREATE DATABASE DNAPICE;
USE DNAPICE;

CREATE TABLE Bioma (
    id_bioma INT PRIMARY KEY,
    flora VARCHAR(100),
    clima VARCHAR(100),
    fauna VARCHAR(100),
    nome VARCHAR(100),
    horario TIME,
    estacao VARCHAR(50),
    umidade FLOAT,
    temperatura FLOAT
);

CREATE TABLE Corpo_Humano (
    id_corpo INT PRIMARY KEY,
    cpf VARCHAR(11),
    saturacao_de_oxigenio FLOAT,
    pressao_arterial VARCHAR(20),
    nome VARCHAR(100),
    hidratacao FLOAT,
    temperatura_corpo FLOAT,
    bioma_atual INT,
    FOREIGN KEY (bioma_atual) REFERENCES Bioma(id_bioma)
);

-- Tabela Pulmao
CREATE TABLE Pulmao (
    id_pulmao INT PRIMARY KEY,
    estado_saude VARCHAR(100),
    id_corpo INT UNIQUE,
    FOREIGN KEY (id_corpo) REFERENCES Corpo_Humano(id_corpo)
);

-- Tabela Rins
CREATE TABLE Rins (
    id_rins INT PRIMARY KEY,
    filtracao FLOAT,
    id_corpo INT UNIQUE,
    FOREIGN KEY (id_corpo) REFERENCES Corpo_Humano(id_corpo)
);

-- Tabela Sistema Excretor
CREATE TABLE Sistema_Excretor (
    id_sistema_excretor INT PRIMARY KEY,
    capacidade_maxima_urina FLOAT,
    testar_cheia BOOLEAN,
    id_corpo INT UNIQUE,
    FOREIGN KEY (id_corpo) REFERENCES Corpo_Humano(id_corpo)
);

-- Tabela Deserto
CREATE TABLE Deserto (
    id_bioma INT PRIMARY KEY,
    temperatura_dia FLOAT,
    temperatura_noite FLOAT,
    FOREIGN KEY (id_bioma) REFERENCES Bioma(id_bioma)
);

-- Tabela Taiga
CREATE TABLE Taiga (
    id_bioma INT PRIMARY KEY,
    FOREIGN KEY (id_bioma) REFERENCES Bioma(id_bioma)
);

-- Tabela Tundra
CREATE TABLE Tundra (
    id_bioma INT PRIMARY KEY,
    altitude_metros FLOAT,
    velocidade_vento FLOAT,
    FOREIGN KEY (id_bioma) REFERENCES Bioma(id_bioma)
);

-- Cadastro dos biomas
INSERT INTO Bioma (id_bioma, flora, clima, fauna, nome, horario, estacao, umidade, temperatura)
VALUES
(1, 'Cactos e arbustos', 'Arido', 'Repteis e roedores',
 'Deserto', '12:00:00', 'Verao', 15, 40),

(2, 'Coniferas', 'Frio e subartico', 'Alces e ursos',
 'Taiga', '12:00:00', 'Inverno', 60, -10),

(3, 'Musgos e liquens', 'Polar', 'Renas e raposas-do-artico',
 'Tundra', '12:00:00', 'Inverno', 40, -20);


-- Cadastro das caracteristicas especificas do Deserto
INSERT INTO Deserto (id_bioma, temperatura_dia, temperatura_noite) VALUES (1, 40, 20);


-- Cadastro da Taiga
INSERT INTO Taiga (id_bioma) VALUES (2);


-- Cadastro das caracteristicas especificas da Tundra
INSERT INTO Tundra (id_bioma, altitude_metros, velocidade_vento) VALUES (3, 500, 30);