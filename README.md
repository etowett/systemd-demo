# Systemd Example

This app demonstrate how to run a python app as a systemd daemon.

The app will run every 5 seconds. Its like running a cron every 5 seconds.

You can control the app with systemd commands

```
    systemctl restart complex
    systemctl start complex
    systemctl stop complex
    systemctl enable complex
```

Logs will go to `/var/log/messages` and will be managed by `journalctl` e.g `journalctl -u complex -f` to follow this app specific logs
