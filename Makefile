
clean:
	rm -f  multiple_ip_to_dns*.csv unresolved_ip_to_dns*.csv summary*.txt resolved_ip_to_dns*.csv port_443_*.csv port_80_*.csv both_ports*.csv

rmDns:
	rm -f  multiple_ip_to_dns*.csv unresolved_ip_to_dns*.csv summary_dns*.txt resolved_ip_to_dns*.csv

rmPort:
	rm -f port_443_*.csv port_80_*.csv both_ports*.csv summary_port*.txt

successIps:
	python ip_to_dns.py tmp.csv
	python port.py resolved_ip_to_dns*.csv

errorIp:
	python ip_to_dns.py tmp.csv
	python port.py unresolved_ip_to_dns*.csv

port80:
	python port.py tmp.csv
	python ip_to_dns.py port_80_*.csv

port443:
	python port.py tmp.csv
	python ip_to_dns.py port_443_*.csv
