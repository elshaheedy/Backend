CREATE TABLE `Doctor` (
  `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `speciality` varchar(255),
  `license_number` varchar(255),
  `id_profile` INT
);

CREATE TABLE `medical_record` (
  `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `patient_id` INT NOT NULL,
  `Temprature` varchar(255),
  `pulse` varchar(255),
  `blood_pressure` varchar(255),
  `description` varchar(255),
  `created_at` timestamp NOT NULL,
  `updated_at` timestamp NOT NULL,
  `is_deleted` bool
);

CREATE TABLE `Address` (
  `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `street` varchar(255),
  `city` varchar(255),
  `governorate` varchar(255),
  `created_at` timestamp NOT NULL,
  `updated_at` timestamp NOT NULL,
  `is_deleted` bool
);

CREATE TABLE `File` (
  `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `name` varchar(255),
  `path` varchar(255),
  `created_at` timestamp NOT NULL,
  `updated_at` timestamp NOT NULL,
  `is_deleted` bool
);

CREATE TABLE `Visit` (
  `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `doctor_id` INT NOT NULL,
  `file_id` INT,
  `patient_id` INT NOT NULL,
  `medical_record_id` INT,
  `tickets_number` INT,
  `created_at` timestamp NOT NULL,
  `updated_at` timestamp NOT NULL,
  `is_deleted` bool
);

CREATE TABLE `Patient` (
  `profiel_id` INT NOT NULL,
  `address_id` INT,
  `nationality` varchar(255),
  `blood_type` varchar(255),
  `created_at` timestamp NOT NULL,
  `updated_at` timestamp NOT NULL
);

CREATE TABLE `Phone` (
  `mobile` varchar(255) NOT NULL,
  `verifed` bool NOT NULL,
  `user` INT NOT NULL,
  `created_at` timestamp NOT NULL,
  `updated_at` timestamp NOT NULL,
  `is_deleted` bool
);

CREATE TABLE `Profile` (
  `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `image` varchar(255),
  `date_of_birth` DATE NOT NULL,
  `gender` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL,
  `user_id` INT NOT NULL,
  `updated_at` timestamp NOT NULL
);

CREATE TABLE `User` (
  `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL,
  `updated_at` timestamp NOT NULL,
  `is_deleted` bool
);

ALTER TABLE `Address` ADD CONSTRAINT `FK_Patient_TO_Address` FOREIGN KEY (`id`) REFERENCES `Patient` (`address_id`);

CREATE TABLE `Visit_Doctor` (
  `Visit_doctor_id` INT,
  `Doctor_id_profile` INT,
  PRIMARY KEY (`Visit_doctor_id`, `Doctor_id_profile`)
);

ALTER TABLE `Visit_Doctor` ADD FOREIGN KEY (`Visit_doctor_id`) REFERENCES `Visit` (`doctor_id`);

ALTER TABLE `Visit_Doctor` ADD FOREIGN KEY (`Doctor_id_profile`) REFERENCES `Doctor` (`id_profile`);


ALTER TABLE `File` ADD CONSTRAINT `FK_Patient_TO_File` FOREIGN KEY (`id`) REFERENCES `Visit` (`file_id`);

ALTER TABLE `medical_record` ADD CONSTRAINT `FK_Patient_TO_medical_record` FOREIGN KEY (`id`) REFERENCES `Visit` (`medical_record_id`);

CREATE TABLE `Visit_Patient` (
  `Visit_patient_id` INT,
  `Patient_profiel_id` INT,
  PRIMARY KEY (`Visit_patient_id`, `Patient_profiel_id`)
);

ALTER TABLE `Visit_Patient` ADD FOREIGN KEY (`Visit_patient_id`) REFERENCES `Visit` (`patient_id`);

ALTER TABLE `Visit_Patient` ADD FOREIGN KEY (`Patient_profiel_id`) REFERENCES `Patient` (`profiel_id`);


ALTER TABLE `Profile` ADD CONSTRAINT `FK_Patient_TO_Profile` FOREIGN KEY (`id`) REFERENCES `User` (`id`);

ALTER TABLE `Phone` ADD CONSTRAINT `FK_Profile_TO_Patient` FOREIGN KEY (`user`) REFERENCES `Profile` (`id`);

ALTER TABLE `Doctor` ADD CONSTRAINT `FK_Profile_TO_Doctor` FOREIGN KEY (`id_profile`) REFERENCES `Profile` (`id`);

ALTER TABLE `Patient` ADD CONSTRAINT `FK_Profile_TO_Patient` FOREIGN KEY (`profiel_id`) REFERENCES `Profile` (`id`);
