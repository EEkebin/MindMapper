<!DOCTYPE html>
<!-- svelte-ignore a11y-missing-attribute -->

<head>
	<title>Habit Tracker</title>
</head>

<body>
    <!-- svelte-ignore a11y-missing-attribute -->
    <html>
        <head>
          <title>My Landing Page</title>
          <link rel="stylesheet" type="text/css" href="styles.css">
        </head>
        <body>
          <div class="tiles">
            <div class="tile">
              <h2>Graph Placeholder</h2>
              <div class="graph-placeholder"></div>
            </div>
            <div class="tile">
              <h2>Create Habits</h2>
              <a href="/createHabit"><button>Create</button></a>
            </div>
            <div class="tile">
              <h2>Delete Habits</h2>
              <button>Delete</button>
            </div>
            <div class="tile">
              <h2>Update Current Habits</h2>
              <button>Update</button>
            </div>
          </div>
        </body>
      </html>
</body>

<style>
        body {
        background-color: #f2f2f2;
        font-family: Arial, sans-serif;
    }
.tiles {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  margin-top: 50px;
}

.tile {
  width: 300px;
  height: 200px;
  margin: 20px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  text-align: center;
}

.graph-placeholder {
  width: 100%;
  height: 150px;
  border: 1px dashed #ccc;
  margin-top: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}

button {
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}

button:hover {
  background-color: #0069d9;
}

</style>