# sg_compact_logs

This application is used to collect sync gateway logs from a docker container.
It uses the docker package from python to identify, connect and pull system logs.
Those logs are then filtered on keywords to return log entries relevent to compaction.
The entire application is wrapped in Flask to be used as an api endpoint.
http://<ip or host name>/logs/<name of container>

return:
{
"compaction_logs": [
"system log1....",
"system log2...."
]
}
