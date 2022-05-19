
<h2>These routes create a sample user, sample characters, and sample planets</h2>

<h4>They can be called with the POST Method using an empty body</h4>

1. /createuser (generates one sample user)
2. /createpeople (generates 3 starwars characters with 3 respective IDs)
3. /createplanet (generates 3 starwars planets with 3 respective IDs))



<h2>These routes add favorite planets and favorite characters to the user</h2>

<h4>They use the POST Method and a number in the URL</h4>

1. /favorite/planet/<int:planet_id> (works with an ID number of 1 to 3 and adds a planet to the user favorites)
2. /favorite/people/<int:people_id> (works with an ID number of 1 to 3 and adds a character to the user favorites)




