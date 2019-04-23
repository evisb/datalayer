[![Datalayer](https://docs.datalayer.io/logo/datalayer-25.svg)](https://datalayer.io)

```
chmod 744 /usr/local/bin/kubeadm-join
systemctl daemon-reload
systemctl enable kubeadm-join
systemctl start kubeadm-join
systemctl status kubeadm-join
journalctl -fu kubeadm-join
journalctl -lxeu kubeadm-join
cat /root/kubeadm.conf
cat /root/kubeadm.out
```
