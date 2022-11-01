-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mar. 01 nov. 2022 à 22:56
-- Version du serveur : 5.7.36
-- Version de PHP : 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `docstruc`
--

-- --------------------------------------------------------

--
-- Structure de la table `candicomp`
--

DROP TABLE IF EXISTS `candicomp`;
CREATE TABLE IF NOT EXISTS `candicomp` (
  `idCC` int(11) NOT NULL AUTO_INCREMENT,
  `idCand` int(11) DEFAULT NULL,
  `idComp` int(11) DEFAULT NULL,
  PRIMARY KEY (`idCC`),
  KEY `idCand` (`idCand`),
  KEY `idComp` (`idComp`)
) ENGINE=MyISAM AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `candidats`
--

DROP TABLE IF EXISTS `candidats`;
CREATE TABLE IF NOT EXISTS `candidats` (
  `idCand` int(11) NOT NULL AUTO_INCREMENT,
  `Nom` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Prenom` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Mail` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Tel` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Linkedin` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Github` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`idCand`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `candiform`
--

DROP TABLE IF EXISTS `candiform`;
CREATE TABLE IF NOT EXISTS `candiform` (
  `idCF` int(11) NOT NULL AUTO_INCREMENT,
  `idCand` int(11) DEFAULT NULL,
  `idform` int(11) DEFAULT NULL,
  PRIMARY KEY (`idCF`),
  KEY `idCand` (`idCand`),
  KEY `idform` (`idform`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `competences`
--

DROP TABLE IF EXISTS `competences`;
CREATE TABLE IF NOT EXISTS `competences` (
  `idComp` int(11) NOT NULL AUTO_INCREMENT,
  `NomComp` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`idComp`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `competences`
--

INSERT INTO `competences` (`idComp`, `NomComp`) VALUES
(1, 'Java'),
(2, 'C'),
(3, 'SQL'),
(4, 'Vue.js'),
(5, 'C++'),
(6, 'C#'),
(7, 'JavaScript'),
(8, 'Python'),
(9, '.NET'),
(10, 'Spring'),
(11, 'SpringBoot'),
(12, 'JS'),
(13, 'Anglais'),
(14, 'Espagnol'),
(15, 'Arabe'),
(16, 'Chinois'),
(17, 'Allemand'),
(18, 'Italien'),
(19, 'PHP'),
(20, 'CSS'),
(21, 'HTML'),
(22, 'Web');

-- --------------------------------------------------------

--
-- Structure de la table `formations`
--

DROP TABLE IF EXISTS `formations`;
CREATE TABLE IF NOT EXISTS `formations` (
  `idForm` int(11) NOT NULL AUTO_INCREMENT,
  `NomForm` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`idForm`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
