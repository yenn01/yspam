<script>
	export let name;


</script>

<main>
	<!-- <h1>Hello {name}!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p> -->
</main>

<body>
	<div class="header">
		<p>Y5 Securities</p>
		<p>World's Best Scam Detection Platform</p>
	</div>
	<div class="form">
		<div>
			<h2>Y5 Securities</h2>
			<img src="favicon.png" height="150" width="150"/>
			<h1>Scam Detector</h1>
			<p class="slogan">Can't tell which are scam texts? <br> Paste them below to check <br></p>
			<form action="">
				<div class="in-form">
					<div class="input_container">
						<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="search_icon" viewBox="0 0 24 24">
							<path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
						</svg>
						<input class="search_input" type="text" placeholder="Enter text here">
						<button class="search_btn" type="submit">Check</button>
					</div>
				</div>
			</form>
		</div> 
	</div>
	<div class="meter">
		<meter value="0.5" ></meter>
	</div>
</body>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	body{
		background-color: rgb(224, 227, 230);
	}

	h1 {

		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}

	.form{
		color: whitesmoke;
		padding-top: 100px;
		background-color: darkcyan;
		box-sizing: block;
		text-align: center;
	}

	.slogan {
		font-size: 23px;
	}

	form{
		width: 100%;
		margin: 0px auto;
	}

	.in-form {
		display: block;
		box-sizing: inherit;
		padding-bottom: 5%;
	}


	.input_container {
		width: 60%;
		margin-left: 20%;
		margin-left: 20%;
		position: relative;
		background-color: white;
		padding: 20px, 150px, 20px, 70px;
		font-size: 20px;
		color: black;
		border-radius: 20px;
		display: flex;
		flex-wrap: wrap;
		align-items: center;
		overflow: hidden;
		-webkit-transition: all 0.3s;

	}

	.search_input{
		margin: 0;
		padding-top: 1%;
		padding-bottom: 1%;
		font-size: 20px;
		width: 90%;
		vertical-align: middle;
		border: 0;
		box-shadow: none;
		outline: none;
	}



	.search_btn{
		margin: 0;
		height: 100%;
		right: 0;
		top: 0;
		padding-top: 1%;
		padding-bottom: 1%;
		border-radius: 2px;
		justify-content: center;
		position: absolute;
		cursor: pointer;
		align-items: center;
		display: flex;
	}

	.search_icon{
		height: 100%;
		width: 3vw;
		margin: 0;
		color: black;
		margin-left: 0%;
		padding-top: 2%;
		padding-bottom: 0.5%;
		padding-left: 1%;
	}

	.meter {
		padding-top: 5%;
		text-align: center;
	}

	meter {
		width: 500px;
		height: 100px;
	}
</style>