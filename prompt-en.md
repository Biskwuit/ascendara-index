Code me a Python game-site scraper.

It must include a progress bar to track how many games have been scraped. The website uses Cloudflare protection, so use cloudscraper. Also add configurable parameters that I can easily modify, such as:

Adding an X-second delay every X games to avoid rate limits or restrictions.
Configuring the number of concurrent workers.

If the scraper cannot find a specific piece of information, it should completely remove that field from the output template.

Example:

If the scraper cannot find the game size, this line should be removed:

"size": ""

Scraped games must be stored using the following template:

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
      "version": "1.0.0"
    }
  ]
}

Download links example:

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
}

Here is the page that contains all the games to scrape:

https://steamrip.com/games-list-page/

You can find all games on this page. They are listed as follows:

<li class="az-list-item">
  <a href="/007-first-light-free-download/">
    007 First Light Free Download
  </a>
</li>

Here is an example game page containing the game information:

https://steamrip.com/007-first-light-free-download/

And here is where you can find the download links:

<h4><span style="font-size: 18pt;">SYSTEM REQUIREMENTS</span></h4>

...

<h4><span style="font-size: 18pt;">GAME INFO</span></h4>

<div class="plus tie-list-shortcode">
  <ul>
    <li><strong>Genre:</strong> Action, Adventure</li>
    <li><strong>Developer:</strong> IO Interactive A/S</li>
    <li><strong>Platform:</strong> PC</li>
    <li><strong>Game Size:</strong> 49.2 GB</li>
    <li><strong>Released By:</strong> voices38</li>
    <li><strong>Version:</strong> v1.0.0 (Build 23388781)</li>
  </ul>
</div>

<p style="text-align: center;">
  <strong>GOFILE</strong><br/>
  <a href="//gofile.io/d/lrITJ8">DOWNLOAD HERE</a>
</p>

<p style="text-align: center;">
  <strong>BZZHR</strong><br/>
  <a href="//bzzhr.to/rcby3xmpgwb4">DOWNLOAD HERE</a>
</p>

<p style="text-align: center;">
  <strong>FileDitch</strong><br/>
  <a href="//fileditchfiles.me/alpha7/...">DOWNLOAD HERE</a>
</p>

Convert URLs that start with // into https://.

Example:

//gofile.io/d/lrITJ8 → https://gofile.io/d/lrITJ8

Make sure the extracted links are actual download links.

Examples:

https://gofile.io/d/lrITJ8 → valid download link ✔
https://shared.akamai.steamstatic.com/store_item_assets/...jpg → not a download link ✘

Only extract links from the DOWNLOAD section.

According to the template, every game title may contain "Free Download" and additional version information. You must remove "Free Download" and everything that follows it from the final game name.

Examples:

007 First Light Free Download → 007 First Light
20 Minutes Till Dawn Free Download (v1.0.2) → 20 Minutes Till Dawn

To determine whether a game supports multiplayer (online: true), inspect the original title before formatting.

Examples:

MECCHA CHAMELEON Free Download (v1.8.0 + Multiplayer)
Dying Light 2 Stay Human Free Download (v1.28.0c + Co-op)

Both should result in:

"online": true

To determine whether a game includes DLCs (dlc: true), use the same approach.

Examples:

HITMAN 2 Free Download (v2.72.0 & ALL DLC)
Yasuke Simulator: Digital Deluxe Edition (3 DLCs)
Call of Duty: Black Ops II Free Download (Multiplayer + DLCs)

All should result in:

"dlc": true

The template also requires the date of the latest update. This can be found on the game page in formats such as:

<span class="date meta-item tie-icon">12 seconds ago</span>
<span class="date meta-item tie-icon">2 weeks ago</span>
<span class="date meta-item tie-icon">22 hours ago</span>
<span class="date meta-item tie-icon">2 days ago</span>
<span class="date meta-item tie-icon">June 8, 2023</span>

Convert all of these formats into a standardized date string:

"latest_update": "YYYY-MM-DD"

Feel free to ask me for additional information if needed. If there is not enough information to fully complete the script, let me know.
