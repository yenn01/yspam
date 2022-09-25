<script>
	export let name;
    import { fade, fly } from 'svelte/transition';
    import {Stretch} from 'svelte-loading-spinners';
    import anime from 'animejs/lib/anime.es.js';
    import Toast from "./components/Toast.svelte";
    import {notifications} from './stores/notifications.js'

    $: src = "./logo_ham.png"
    let inputText = ''
    $: results = 'F';
    $: loading = false;
    $: ham = 0;
    $: spam = 0;
    $: text = '';
    $: show = false;
    let response;
    $: textAreaColor = 'rgb(243, 243, 243)';
    $: textAreaSize = 5;
    $: textLength = inputText.length;

    $: textLength, emptyArea();
    $: inputText,setSize();


    const change = () => {
        let hamPercent = Math.round(response.ham*100 * 100) / 100
        
        let spamPercent = Math.round(response.spam*100 * 100) / 100
        ham = response.ham
        spam = response.spam
        anime({
            targets: '#progress',
            width: `${hamPercent}%`,
            easing: 'easeOutExpo',
            duration:4000
        })
        anime({
            targets: '#hamPercent',
            innerHTML: [0,hamPercent],
            easing: 'easeOutExpo',
            round:100,
            duration:3000,
            
        })
        anime({
            targets: '#spamPercent',
            innerHTML: [0,spamPercent],
            easing: 'easeOutExpo',
            round:100,
            duration:3000,
            
        })
        



        if(response.spam > response.ham) {
            src = "./logo_spam.png"
            results = 'S';
            text = 'Likely Spam'
            textAreaColor = '#d55252'
        } else if (response.ham > response.spam) {
            src = "./logo_ham.png"
            results = 'H';
            text = 'Likely Safe'
            textAreaColor = '#41ee9c'
        } 
    }


    const setSize = () => {
        if (textLength < 10) {
            textAreaSize = 5;
        } else if (textLength < 20) {
            textAreaSize = 4;
        } else if (textLength < 40) {
            textAreaSize = 3.5;
        } else if (textLength < 55) {
            textAreaSize = 3;
        } else if (textLength < 130) {
            textAreaSize = 2;
        } else if (textLength < 200) {
            textAreaSize = 1.7;
        } else if (textLength < 300) {
            textAreaSize = 1.4;
        } else {
            textAreaSize = 1.2;
        }
    }

    function reset() {
        
        src = "./logo_ham.png"
        textAreaColor = 'rgb(243, 243, 243)'
        results ='F'
        show = false;
    }

    function emptyArea() {
        if(textLength<=0) {
            reset()
        }
    }

    async function getPrediction() {
        if(textLength <= 0) {
            notifications.danger('No message passed', 4000)
            return;
        }
        reset()
        loading = true;
        results = 'L'
        console.log(encodeURI(inputText))
        let url = "/analyse?text="+encodeURI(inputText)
        const res = await fetch(url).then(res => res.json()).then(
			parsed => {
                    response = arrMerge(parsed.labels,parsed.scores)
                    show = true;
                    loading=false;
                    
                   console.log(JSON.stringify(response))
            }
		).catch((e)=> {
            show = false
            loading = false;
            console.error(e)
        });
        
    }

    function arrMerge(k, v) {

        var obj = {};

        for (var i = 0; i < k.length; i++) {
            obj[k[i]] = v[i];
        }

        return obj;
    }

    
</script>

<svelte:head>
    <title>spam?</title>
</svelte:head>

<main>
    <Toast/>
	<div class="main-container">
        <div class="top-container">
			<img class="logo" {src} transition:fade/>
            <div class="state-holder" >
                {#if results === 'F'}
                    <p class="slogan state-item" transition:fade>Can't differentiate <strong>spam</strong> texts? </p>
                {:else if results === 'H'}
                    <p class="slogan state-item" transition:fade>Most likely it's <strong style="color:#45ea81;">okay</strong>!</p>
                {:else if results === 'S'}
                    <p class="slogan state-item" transition:fade>Be careful ! It's most likely <strong style="color:#d55252;">spam</strong>.</p>
                {:else if results === 'L'}
                    <p class="slogan state-item" transition:fade>Please wait while we <strong>investigate</strong>.</p>
                {/if}
            </div>
            <small>Paste them below to check </small>
				<div class="in-form">
                    <textarea class="input-area" style="font-size:{textAreaSize}rem; transition: 0.5s; border:4px solid {textAreaColor};" bind:value={inputText} transition:fade placeholder="Type here..."></textarea>
					<p class="length"> {textLength} chars</p>
                    <div class="state-holder">
                        {#if loading === false}
                            <button class="search_btn state-item" type="submit" on:click={getPrediction} transition:fade>
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="white" class="search_icon" viewBox="-1 -3 24 24">
                                    <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
                                </svg>
                                <div class="inner_btn" transition:fade> Check</div>	
                            
                            </button>
                        {:else}
                            <div class="state-item"><Stretch color="#41ee9c"></Stretch></div>
                        {/if}
                    </div>
				</div>
        </div>
        {#if show === true}
        <div class="progress-holder" transition:fly="{{ y: 50, duration: 500 }}" on:introend={change}>
            <div class="progress-bar progress-background"></div>
            <div class="progress-bar progress-front" id="progress"></div>
            <div class="progress-ham"><strong id="hamPercent">0</strong> %</div>
            <div class="progress-text" style="color:{ ham > spam ? '#41ee9c' : spam > ham ?'#d55252' : 'rgb(243, 243, 243)'}"><strong transition:fade>{text}</strong></div>
            <div class="progress-spam"><strong id="spamPercent">0</strong> %</div>
        </div>
        {/if}
	</div>
	
	
</main>
<footer>
	<small>All Rights Reserved | &copy; 2022 y spam?</small>
</footer>

	

<style>
    @import url('https://fonts.googleapis.com/css2?family=Lora&family=Playfair+Display&display=swap');


    footer {
        color:rgb(243, 243, 243);
        text-align:center;
    }

    small {
        color:rgb(243, 243, 243);
    }

    .progress-holder {
        display:grid;
        grid-template-columns: repeat(3, 2fr);
        grid-template-rows: repeat(2, 3fr);
        width:50%;
        height:50px;

    }

    .progress-bar {
        
        grid-column: 1/4;
        grid-row: 1/2;
    }

    .progress-ham {
        grid-column: 1/2;
        grid-row: 2/3;
        color :#41ee9c;
        text-align: left;
    }

    .progress-spam {
        grid-column: 3/4;
        grid-row: 2/3;
        color :#d55252;
        text-align:right;
    }

    .progress-text {
        grid-column: 2/3;
        grid-row: 2/3;    
        color:rgb(243, 243, 243);    
    }

    .top-container {
        display: flex;
        align-items: center;
        flex-direction: column;
        margin-bottom:1em;
    }

    .progress-front {
        background-color: #41ee9c;
        border-radius: 20px;
        height:10px;
        width:1%;
    }

    .progress-background {
        background-color: #d55252;
        border-radius: 20px;
        height:10px;
    }

    .state-holder {
        display:grid;
        grid-template-columns: 1fr;
        grid-template-rows: 1fr;
    }

    .state-item {
        grid-column: 1/2;
        grid-row: 1/2;
    }

    .input-area {
        border-radius: 10px;
        background-color: #cecece;
        resize: none;
        width:50vw;
        height:24vh;
        font-family: 'Lora',serif;
        margin:0;
    }

    .inner_btn {
        min-width: 50px;
        color:white;
        font-size: 1.3rem;
        font-family: 'Lora',serif;
    }

    .length {
        margin-bottom: 1.5em;
    }

    :global(body) {
        background: #191919;
    }

    .logo {
        width:40vw;
    }

    strong {
        font-weight: 2000;
        font-size:1.5rem;
    }

    p {
        font-family: 'Lora', serif; 
        color: rgb(243, 243, 243);
    }

	main {
		text-align: center;
		padding: 0.2em;
		max-width: 500px;
		margin: 0 auto;
        min-width: 500px;
        min-height: 95vh;
	}

	@media (min-width: 500px) {
		main {
			max-width: none;
		}

        
	}

    @media(max-width:600px) {
        .input-area {
            width: 70vw;
        }
    }

    .search_btn {
        display:flex;
        flex-direction: row;
        align-items: center;
        min-width: 200px;
        justify-content: center;
        border-radius: 20px;
        background: none;
        border: 2px solid white;
        
    }

    .search_btn:hover {
        background-color: #41ee9c;
        transition: 0.3s;
        cursor:pointer;
    }

	.main-container{
		display:flex;
        flex-direction: column;
        align-items: center;
	}

	.slogan {
		font-size: 1.3rem;
	}


	.in-form {
		display: flex;
        flex-direction: column;
        align-items: center;
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
		width: 500px;
		height: 100px;
	}
</style>