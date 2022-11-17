-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : jeu. 17 nov. 2022 à 08:16
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
) ENGINE=MyISAM AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `candicomp`
--

INSERT INTO `candicomp` (`idCC`, `idCand`, `idComp`) VALUES
(100, 16, 1),
(99, 16, 20),
(98, 16, 21),
(97, 16, 3),
(96, 16, 8),
(95, 16, 14),
(94, 16, 13),
(93, 16, 2),
(92, 15, 14),
(91, 15, 7),
(90, 15, 1),
(89, 15, 20),
(88, 15, 19),
(87, 15, 21),
(86, 15, 13),
(85, 15, 2),
(84, 14, 14),
(83, 14, 13),
(82, 14, 2),
(81, 13, 3),
(80, 13, 1),
(79, 13, 20),
(78, 13, 8),
(77, 13, 14),
(76, 13, 13),
(75, 13, 2),
(74, 12, 14),
(73, 12, 13),
(72, 12, 2),
(71, 11, 1),
(70, 11, 20),
(69, 11, 21),
(68, 11, 3),
(67, 11, 8),
(66, 11, 14),
(65, 11, 13),
(64, 11, 2),
(63, 10, 21),
(62, 10, 20),
(61, 10, 3),
(60, 10, 1),
(59, 10, 18),
(58, 10, 13),
(57, 10, 8),
(56, 10, 2),
(55, 9, 21),
(54, 9, 20),
(53, 9, 19),
(52, 9, 1),
(51, 9, 2);

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
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `candidats`
--

INSERT INTO `candidats` (`idCand`, `Nom`, `Prenom`, `Mail`, `Tel`, `Linkedin`, `Github`) VALUES
(15, 'Monnet', 'Jean', 'jeoffrey.pereira@live.fr', '0755800268', 'www.linkedin.com/in/jeoffre', NULL),
(14, 'Brun,', 'Emmanuel', 'jocelyn.hauf@gmail.com', '0695140092', NULL, NULL),
(13, 'Né', 'Jocelyn', 'jocelyn.hauf@gmail.com', '0695140092', NULL, NULL),
(12, 'Formations', 'Jocelyn', 'jocelyn.hauf@gmail.com', '0695140092', NULL, NULL),
(11, 'En', 'Jocelyn', 'jocelyn.hauf@gmail.com', '0695140092', NULL, NULL),
(10, 'E´tudiant', 'Ian', 'riviere.ian@free.fr', '076812060696', 'https://www.linkedin.com/in/riverian2/', 'https://github.com/Mic-Firapat'),
(9, '20', 'Arthur', 'arthurmicol@gmail.com', '0770728992', NULL, NULL),
(16, 'En', 'Jocelyn', 'jocelyn.hauf@gmail.com', '0695140092', NULL, NULL);

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
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `candiform`
--

INSERT INTO `candiform` (`idCF`, `idCand`, `idform`) VALUES
(1, 9, 4),
(2, 10, 2),
(3, 10, 1),
(4, 11, 2),
(5, 11, 1),
(6, 12, 1),
(7, 12, 2),
(8, 13, 1),
(9, 15, 1),
(10, 15, 4),
(11, 15, 6),
(12, 16, 2),
(13, 16, 1);

-- --------------------------------------------------------

--
-- Structure de la table `competences`
--

DROP TABLE IF EXISTS `competences`;
CREATE TABLE IF NOT EXISTS `competences` (
  `idComp` int(11) NOT NULL AUTO_INCREMENT,
  `NomComp` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`idComp`)
) ENGINE=MyISAM AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

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
(22, 'Web'),
(23, 'Cobol'),
(24, 'Latex'),
(25, 'Progress'),
(26, 'Dart'),
(27, 'Flutter'),
(28, 'xamarin'),
(29, 'android'),
(30, 'Bash'),
(31, 'React'),
(32, 'NodeJs'),
(33, 'Angular'),
(34, 'TypeScript'),
(35, 'Marketing'),
(36, 'Comptabilité'),
(37, 'Management'),
(38, 'Marouflage');

-- --------------------------------------------------------

--
-- Structure de la table `formations`
--

DROP TABLE IF EXISTS `formations`;
CREATE TABLE IF NOT EXISTS `formations` (
  `idForm` int(11) NOT NULL AUTO_INCREMENT,
  `NomForm` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`idForm`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `formations`
--

INSERT INTO `formations` (`idForm`, `NomForm`) VALUES
(1, 'Licence'),
(2, 'Master'),
(3, 'Doctorat'),
(4, 'DUT'),
(5, 'BTS'),
(6, 'BAC'),
(7, 'Brevet'),
(8, 'CAP'),
(9, 'BEP');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
