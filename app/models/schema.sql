INSERT INTO team (name)
VALUES ('linz');

use sportsdb; 

CREATE TABLE IF NOT EXISTS sport (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS team (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS event (
  id INT AUTO_INCREMENT PRIMARY KEY,
  event_date DATE NOT NULL,
  event_time TIME NOT NULL,
  sport_id INT,
  FOREIGN KEY (sport_id) REFERENCES sport(id)
);

CREATE TABLE IF NOT EXISTS event_team (
  event_id INT,
  team_id INT,
  PRIMARY KEY (event_id, team_id),
  FOREIGN KEY (event_id) REFERENCES event(id),
  FOREIGN KEY (team_id) REFERENCES team(id)
);