-- phpMyAdmin SQL Dump
-- version 4.2.12deb2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 07, 2015 at 05:54 PM
-- Server version: 5.5.43-0+deb8u1
-- PHP Version: 5.6.7-1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `events`
--

-- --------------------------------------------------------

--
-- Table structure for table `EVENT`
--

CREATE TABLE IF NOT EXISTS `EVENT` (
`EVENTS_PUID` int(11) NOT NULL,
  `EVENTS_START_TIME` time DEFAULT NULL,
  `EVENTS_START_DAY` date DEFAULT NULL,
  `EVENTS_END_TIME` time DEFAULT NULL,
  `EVENTS_END_DAY` date DEFAULT NULL,
  `EVENTS_DESC` text,
  `EVENTS_CREATE_DATE` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `EVENTS_TITLE` varchar(45) DEFAULT 'MY NEW EVENT',
  `GOO_EVENT_ID` varchar(1024) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `EVENT`
--

INSERT INTO `EVENT` (`EVENTS_PUID`, `EVENTS_START_TIME`, `EVENTS_START_DAY`, `EVENTS_END_TIME`, `EVENTS_END_DAY`, `EVENTS_DESC`, `EVENTS_CREATE_DATE`, `EVENTS_TITLE`, `GOO_EVENT_ID`) VALUES
(1, '07:00:00', '2015-06-09', '09:00:00', '2015-06-09', 'Doctor must meet Patient 1, and a very long text follows', '2015-06-07 12:51:27', 'Meeting with Patient 1', 'v65iek7jnddncan8todl2tmd0c'),
(4, '12:00:00', '2015-06-08', '16:00:00', '2015-06-08', 'Association of medical body', '2015-06-07 12:59:54', 'Meeting with Assoc.', 'fl6r9lvdpind1io3eo5vfimqhs'),
(16, '07:00:00', '2015-06-05', '09:30:00', '2015-06-05', 'my description here about banana', '2015-06-07 12:59:54', 'banana doctor', 'gvrmf0vf8fubjuf5cqudg0tqjo'),
(19, '10:00:00', '2015-06-09', '12:30:00', '2015-06-09', 'Doctor must meet Patient 2, and a very long text follows', '2015-06-07 12:51:32', 'Meeting with Patient 2', '5b2fsfq1s6ldcbuv42e339n4tc');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `EVENT`
--
ALTER TABLE `EVENT`
 ADD PRIMARY KEY (`EVENTS_PUID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `EVENT`
--
ALTER TABLE `EVENT`
MODIFY `EVENTS_PUID` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=24;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
