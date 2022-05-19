
<h2>These routes create a sample user, sample characters, and sample planets</h2>

<h4>They can be called with the POST Method using an empty body</h4>

1. /createuser (generates one sample user)
2. /createpeople (generates 3 starwars characters with 3 respective IDs)
3. /createplanet (generates 3 starwars planets with 3 respective IDs))



<h2>These routes add planets and characters to the user favorites</h2>

<h4>They use the POST Method and a number in the URL</h4>

1. /favorite/planet/<int:planet_id> (works with an ID number of 1 to 3 and adds a planet to the user favorites)
2. /favorite/people/<int:people_id> (works with an ID number of 1 to 3 and adds a character to the user favorites)


<h2>These routes display info about the user, planets, and characters</h2>

<h4>They use the GET Method and some use a number in the URL</h4>

1. /users/favorites (shows the planets and characters added to the user favorites)
2. /users (shows all the users in the database)
3. /users/<int:id> (works with an ID number of 1 only, and shows user info)
4. /people (shows all the characters in the database)
5. /people/<int:id> (works with an ID number of 1 to 3 and shows one character)
6. /planets (shows all the planets in the database)
7. /planets/<int:id> (works with an ID number of 1 to 3 and shows one planet)


<h2>These routes delete planets and characters from the user favorites</h2>

<h4>They use the DELETE Method and a number in the URL</h4>

1. /favorite/planet/<int:planet_id> (works with an ID number of 1 to 3 and deletes a planet from the user favorites)
2. /favorite/people/<int:character_id> (works with an ID number of 1 to 3 and deletes a character from the user favorites)






