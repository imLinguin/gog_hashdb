# gog hashdb

## What is it?
GOG's hashdb is a very simple format providing checksums for each file from given product depot

`goggame-GameId.hashdb`


## Structure

hashdb is a zip file with one entry (called the same as archive)

### Header
File starts with 3, 4-byte intigers. First two are always `12` and `1`

The third intiger is number of records


### File record

Each record is a `1024` byte file path relative to install directory.  
And `32` bytes of MD5 checksum.

