Code moi un scrappeur de sites de jeux en python. 
Il faut une barre de progression pour suivre le nombre de jeux scrappés, de plus le site utilise une protection cloudflare alors utilise 'cloudscraper' et rajoute des paramètres que je peux modifier pour par exemple si je veux rajouter X secondes de délai tout les X jeux pour éviter les restrictions et une option pour configurer le nombre de workers at a time. 
Si le scrappeur ne trouve pas une info alors il supprime la ligne sur la template Ex : Le scrappeur ne trouve pas la taille du jeu, cette ligne dissparaît : ' "size": "",'. 
Les jeux une fois scrappés doivent être rangés selon cette template : 

{
  "games": [
    {
      "category": ["Action", "Adventure", "Indie"],
      "dirlink": "https://example.com/game-download/",
      "dlc": false,
      "download_links": {},
      "game": "Sample Game",
      "latest_update": "2026-04-21",
      "minReqs": {
        "cpu": "Intel Core i5 or equivalent",
        "directx": "Version 11",
        "gpu": "NVIDIA GeForce GTX 1060 or equivalent",
        "os": "Windows 10 64-bit",
        "ram": "8 GB RAM",
        "storage": "10 GB available space"
      },
      "online": false,
      "releasedBy": "Sample Group",
      "size": "15.0 GB",
      "version": "1.0.0",
    }
  ]
}

Download Links Example : 

      "download_links": {
        "buzzheavier": [
          "https://buzzheavier.com/t9ciy8yhac0d"
        ],
        "gofile": [
          "https://gofile.io/d/9KrtTk"
        ],
        "megadb": [
          "https://megadb.net/wlswx80x86a0"
        ]
      },
	  
Voici les pages à scraper : https://steamrip.com/games-list-page/ 
Tu peux trouver tout les jeux sur cette page, ils sont formattés comme ça : 

<li class="az-list-item"><a href="/007-first-light-free-download/">007 First Light Free Download</a></li>
<li class="az-list-item"><a href="/1-trait-escape-free-download/">1 Trait Escape Free Download (v1.15)</a></li>
<li class="az-list-item"><a href="/100-orange-juice-free-download/">100% Orange Juice Free Download (Build 13623225)</a></li>
<li class="az-list-item"><a href="/11f-free-download/">11F Free Download</a></li><li class="az-list-item"><a href="/12-is-better-than-6-free-download/">12 is Better Than 6 Free Download</a></li>
<li class="az-list-item"><a href="/1348-ex-voto-free-download/">1348 Ex Voto Free Download</a></li>
<li class="az-list-item"><a href="/20-minutes-till-dawn-free-download-n1/">20 Minutes Till Dawn Free Download (v1.0.2)</a></li>
<li class="az-list-item"><a href="/2dark-free-download/">2Dark Free Download</a></li>
<li class="az-list-item"><a href="/3-minutes-to-midnight-a-comedy-graphic-adventure-free-download/">3 Minutes to Midnight – A Comedy Graphic Adventure Free Download</a></li>
<li class="az-list-item"><a href="/30xx-free-download-1s/">30XX Free Download (v1.3.0)</a></li>
<li class="az-list-item"><a href="/5d-chess-with-multiverse-time-travel-free-download-p1/">5D Chess With Multiverse Time Travel Free Download (v1.1.00f)</a></li>
<li class="az-list-item"><a href="/60-parsecs-free-download-j1/">60 Parsecs! Free Download (Build 22332285)</a></li>
<li class="az-list-item"><a href="/60-seconds-free-download/">60 Seconds! Free Download (Build 8294944)</a></li>
<li class="az-list-item"><a href="/60-seconds-reatomized-free-download-1k/">60 Seconds! Reatomized Free Download (v1.1.9.0)</a></li>
<li class="az-list-item"><a href="/a7-days-to-die-free-download-1i/">7 Days to Die Free Download (v2.6)</a></li>
<li class="az-list-item"><a href="/9-days-free-download/">9 Days Free Download (v1.3)</a></li>
<li class="az-list-item"><a href="/9-kings-free-download/">9 Kings Free Download (v0.7.17)</a></li>
<li class="az-list-item"><a href="/9-years-of-shadows-free-download-n1/">9 Years of Shadows Free Download (v1.1.41)</a></li>
<li class="az-list-item"><a href="/9-bit-armies-a-bit-too-far-free-download-2/">9-Bit Armies: A Bit Too Far Free Download (Build 15494769)</a></li>
<li class="az-list-item"><a href="/911-operator-free-download-y1/">911 Operator Free Download (Build 7533741)</a></li>
</ul></div><div class="az-list-container" data-link="a"><h4 class="az-list-header">A</h4><ul class="az-list">
<li class="az-list-item"><a href="/a-dance-of-fire-and-ice-free-download-1w/">A Dance of Fire and Ice Free Download (Build 8983561)</a></li>
<li class="az-list-item"><a href="/a-day-out-free-download/">A Day Out Free Download (v1.4)</a></li>
<li class="az-list-item"><a href="/a-difficult-game-about-climbing-free-download/">A Difficult Game About Climbing Free Download (v1.138)</a></li>
<li class="az-list-item"><a href="/a-few-quick-matches-free-download/">A Few Quick Matches Free Download (v1.6.1 + Multiplayer)</a></li>
<li class="az-list-item"><a href="/a-game-about-digging-a-hole-free-download/">A Game About Digging A Hole Free Download</a></li>
<li class="az-list-item"><a href="/a-game-about-feeding-a-black-hole-free-download/">A Game About Feeding A Black Hole Free Download</a></li>
<li class="az-list-item">... 

Et voici la page de jeu avec les informations sur le jeu : https://steamrip.com/007-first-light-free-download/ 
et voici où tu peux trouver les liens de téléchargement : 
<div class="clearfix"></div> <hr style="margin-top:0px; margin-bottom:20px;" class="divider divider-solid"> <h4><span style="font-size: 18pt;">SYSTEM REQUIREMENTS</span></h4> <div class="checklist tie-list-shortcode"> <ul class="bb_ul"> <li>Requires a 64-bit processor and operating system</li> <li><strong>OS:</strong> MICROSOFT WINDOWS 10/11, 64-BIT</li> <li><strong>Processor:</strong> INTEL CORE i5 9500, AMD RYZEN 5 3500</li> <li><strong>Memory:</strong> 16 GB RAM</li> <li><strong>Graphics:</strong> NVIDIA GFORCE GTX 1660, AMD RX 5700, INTEL DISCRETE GPU EQUIVALENT</li> <li><strong>Storage:</strong> 80 GB available space</li> <li><strong>Additional Notes:</strong> SSD required</li> </ul> </div> <div class="clearfix"></div> <hr style="margin-top:0px; margin-bottom:20px;" class="divider divider-solid"> <h4><span style="font-size: 18pt;">GAME INFO</span></h4> <div class="plus tie-list-shortcode"> <ul> <li><strong>Genre:</strong> Action, Adventure</li> <li><strong>Developer:</strong> IO Interactive A/S</li> <li><strong>Platform:</strong> PC</li> <li><strong>Game Size: </strong>49.2 GB</li> <li><strong>Released By:</strong> voices38</li> <li><strong>Version</strong>: v1.0.0 (Build 23388781)</li> <li><strong>Pre-Installed Game</strong></li> </ul> </div> <p style="text-align: center;"><span style="color: #ff9900;"><strong>GOFILE</strong></span><br/> <a href="//gofile.io/d/lrITJ8" target="_blank" rel="nofollow" class="shortc-button medium purple ">DOWNLOAD HERE</a> <p style="text-align: center;"><strong>BZZHR</strong><br/> <a href="//bzzhr.to/rcby3xmpgwb4" target="_blank" rel="nofollow" class="shortc-button medium purple ">DOWNLOAD HERE</a> <p style="text-align: center;"><span style="color: #7c6af7;"><strong>FileDitch</strong></span><br/> <a href="//fileditchfiles.me/alpha7/ad39bc302695f0f9bd13/007-First-Light-SteamRIP.com.rar" target="_blank" rel="nofollow" class="shortc-button medium purple ">DOWNLOAD HERE</a> </div> <div id="post-extra-info"> <div class="theiaStickySidebar"> <div class="single-post-meta post-meta clearfix"><span class="author-meta single-author no-avatars"><span class="meta-item meta-author-wrapper meta-author-1"><span class="meta-author"><a href="/author/steamripadmin/" class="author-name tie-icon" title="SteamRIP">SteamRIP</a></span></span></span><span class="date meta-item tie-icon">2 weeks ago</span><div class="tie-alignright"><span class="meta-views meta-item very-hot"><span class="tie-icon-fire" aria-hidden="true"></span> 345,672 </span></div></div> </div> </div> <div class="clearfix"></div> <script id="tie-schema-json" type="application/ld+json"> 

Convertis les URL qui commencent par "//*" en "https://*". Vérifies bien que les liens correspondent bien à un lien de téléchargement Ex : https://gofile.io/d/lrITJ8 : oui | https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3768760/d076a739da6136dc4da2c48750eb6f780d4f826d/ss_d076a739da6136dc4da2c48750eb6f780d4f826d.1920x1080.jpg : non. 
Prends seulement les liens de la section DOWNLOAD. 

Selon la template. Dans chaque nom de jeu tu pourras trouver "Free Download..." Tu dois enlever le "Free Download" Ex : 007 First Light Free Download -> 007 First Light | 20 Minutes Till Dawn Free Download (v1.0.2) -> 20 Minutes Till Dawn. 
Pour trouver si un jeu est Multijoueur ou pas (online or not) tu peux aussi le trouver dans le nom avant le formatage Ex : MECCHA CHAMELEON Free Download (v1.8.0 + Multiplayer) | Dying Light 2 Stay Human Free Download (v1.28.0c + Co-op) 
Pour trouver si un jeu a les DLC, tu peux faire pareil que pour les jeux Multijoueurs Ex : HITMAN 2 Free Download (v2.72.0 & ALL DLC) | Yasuke Simulator: Digital Deluxe Edition (3 DLCs) | Call of Duty: Black Ops II Free Download (Multiplayer + DLCs) 
Et selon la template, tu as aussi besoin de la date de la dernière mise à jour, tu peux la trouver sur la page d'un jeu sous forme : <span class="date meta-item tie-icon">12 seconds ago</span> | <span class="date meta-item tie-icon">2 weeks ago</span> | <span class="date meta-item tie-icon">22 hours ago</span> | <span class="date meta-item tie-icon">2 days ago</span> | <span class="date meta-item tie-icon">June 8, 2023</span> 
N'hésite pas à me demander si tu as besoin de plus d'infos. Si tu n'as pas assez d'infos pour compléter le script en entier, fais le moi savoir.
