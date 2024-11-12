# Movies_to_Torrent_V2
A simple program that searches for movies using YTS API , downloads its .torrent file and then automatically starts to download it using qbittorrent web ui.

# Replace user and password
In Modules.py replace 'user' and 'password' with the username and password of your qbittorrent webui.

---
# rename.py
---
rename.py is an additional file that you may or may not need. This file cleans up the name of the folder and files within that folder and moves it to your desired location. For example: '300 Rise of an Empire (2014) [1080p]' This turns into '300 Rise of an Empire (2014)' and '300.Rise.of.an.Empire.2014.1080p.BluRay.x264.YIFY.mp4' This turns into '300 Rise of an Empire.mp4'

This file is useful if you are using a media server which requires naming to be pretty precise.

markdown

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Search for movies by name.
- Download torrents of selected movies in 1080p quality.
- Simple command-line interface for user interaction.
- Integration with QBittorrent for seamless downloading.

## Requirements

- Python 3.x
- QBittorrent client
- `requests` library
- `qbittorrentapi` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Rorailer/Movie_to_Torrent_V2.git
   ```
2. Install required libraries:
   ```bash
   pip install requests qbittorrentapi
   ```
3. Configure QBittorrent:
   - Ensure QBittorrent is running on your system.
   - Modify the `connection_info` in `Modules.py` to match your QBittorrent settings.

## Usage

1. Run `Main.py`:
   ```bash
   ./Main.py
   ```
2. Choose the search option and enter the movie name.
3. Select a movie from the list and start the download.

## Contributing

Contributions are welcome! If you have suggestions or find any issues, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

Feel free to customize this template with more details about your project, such as usage examples, troubleshooting tips, or additional features.
