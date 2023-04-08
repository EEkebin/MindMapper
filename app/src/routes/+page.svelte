<script>
  let username = '';
  let password = '';

  async function handleSubmit(event) {
    event.preventDefault();

    const response = await fetch(`http://localhost:5000/api/create_user/${username}/${password}`, {
      method: 'POST',
    });

    const data = await response.text();
    console.log(data);
    // Redirect to login page
    window.location.href = '/login';
  }
</script>

<form on:submit={handleSubmit}>
  <input type="text" bind:value={username} placeholder="Username">
  <input type="password" bind:value={password} placeholder="Password">
  <button type="submit">Register</button>
</form>
