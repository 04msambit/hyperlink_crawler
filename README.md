hyperlink_crawler
=================

This will traverse the Web as a linked graph from the starting --url finding all outgoing links (&lt;a> tag): it will store each outgoing link for the URL, and then repeat the process for each or them, until --limit URLs will have been traversed.  The output will be a JSON file with all incoming and outgoing link information
