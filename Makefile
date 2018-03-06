
clean:
	rm -f  multiple_ip_to_dns*.csv unresolved_ip_to_dns*.csv summary*.txt resolved_ip_to_dns*.csv
	rm -f port_443_*.csv port_80_*.csv both_ports*.csv error_open_ports_*.csv open_ports_*.csv json_test_*.csv
	rm -f zgrab_domain_p443_*.csv zgrab_domain_p443_summary_*.txt all_ip_ports_*.csv
	rm -f zgrab_ip_p443_*.csv zgrab_ip_port443_summary_*.txt
	rm -f zgrab_domain_p80_*.csv zgrab_domain_p80_summary_*.txt
	rm -f zgrab_ip_port443_*.csv zgrab_ip_port443_summary_*.txt

cleanDns:
	rm -f  multiple_ip_to_dns*.csv unresolved_ip_to_dns*.csv summary_dns*.txt resolved_ip_to_dns*.csv

cleanPort:
	rm -f port_443_*.csv port_80_*.csv both_ports*.csv summary_port*.txt all_ip_ports_*.csv

cleanOpen:
	rm -f error_open_ports_*.csv open_ports_*.csv

cleanJson:
	rm -f zgrab_domain_p443_*.csv zgrab_domain_p443_summary_*.txt
	rm -f zgrab_ip_p443_*.csv zgrab_ip_port443_summary_*.txt
	rm -f zgrab_domain_p80_*.csv zgrab_domain_p80_summary_*.txt
	rm -f zgrab_ip_port443_*.csv zgrab_ip_port443_summary_*.txt

port80:
	python port.py tmp.csv
	python ip_to_dns.py port_80_*.csv

port443:
	python port.py tmp.csv
	python ip_to_dns.py port_443_*.csv

json443:
	python port.py tmp.csv
	python ip_to_dns.py port_443_*.csv
	./zgrab_domain_port443.sh resolved_ip_to_dns*.csv
	./zgrab_ip_port443.sh unresolved_ip_to_dns*.csv

json80:
		python port.py tmp.csv
		python ip_to_dns.py port_80_*.csv
		./zgrab_domain_port80.sh resolved_ip_to_dns*.csv
		./zgrab_ip_port80.sh unresolved_ip_to_dns*.csv

jsonBothPorts:
		python port.py tmp.csv
		python ip_to_dns.py both_ports*.csv
		./zgrab_domain_port80.sh resolved_ip_to_dns*.csv #to see if they will redirect
		./zgrab_ip_port80.sh unresolved_ip_to_dns*.csv
