#!/usr/bin/env python3
"""
Advanced Port Scanner for CSR Repository
"""

import socket
import threading
import time
from datetime import datetime

class AdvancedPortScanner:
    def __init__(self):
        self.open_ports = []
        self.scan_results = {}
        
        # Common services database
        self.common_services = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
            53: "DNS", 80: "HTTP", 110: "POP3", 443: "HTTPS",
            993: "IMAPS", 995: "POP3S", 3306: "MySQL", 5432: "PostgreSQL",
            3389: "RDP", 5900: "VNC", 27017: "MongoDB"
        }
    
    def get_service_name(self, port):
        """Get service name for port"""
        try:
            return socket.getservbyport(port, 'tcp')
        except:
            return self.common_services.get(port, "Unknown")
    
    def scan_port(self, target, port, timeout=1):
        """Scan a single port"""
        try:
            start_time = time.time()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            
            result = sock.connect_ex((target, port))
            scan_time = round((time.time() - start_time) * 1000, 2)
            
            if result == 0:
                service = self.get_service_name(port)
                self.open_ports.append(port)
                self.scan_results[port] = {
                    'status': 'open',
                    'service': service,
                    'response_time': scan_time
                }
                print(f"✅ Port {port}/tcp - {service} - {scan_time}ms")
            else:
                self.scan_results[port] = {
                    'status': 'closed',
                    'service': 'Unknown',
                    'response_time': scan_time
                }
            
            sock.close()
            
        except Exception as e:
            print(f"❌ Error scanning port {port}: {e}")
    
    def scan_range(self, target, start_port=1, end_port=1000, max_threads=100):
        """Scan a range of ports with threading"""
        print(f"🔍 Starting scan of {target}")
        print(f"🎯 Port range: {start_port}-{end_port}")
        print(f"⏰ Started: {datetime.now()}")
        print("-" * 60)
        
        ports = range(start_port, end_port + 1)
        threads = []
        
        for port in ports:
            while threading.active_count() > max_threads:
                time.sleep(0.1)
            
            thread = threading.Thread(target=self.scan_port, args=(target, port))
            threads.append(thread)
            thread.start()
        
        # Wait for completion
        for thread in threads:
            thread.join()
        
        # Generate report
        self.generate_report(target)
    
    def generate_report(self, target):
        """Generate scan report"""
        print("-" * 60)
        print("📊 SCAN REPORT")
        print("-" * 60)
        print(f"Target: {target}")
        print(f"Scan completed: {datetime.now()}")
        print(f"Open ports found: {len(self.open_ports)}")
        print(f"Scan duration: {self.get_scan_duration()} seconds")
        
        if self.open_ports:
            print("\n📋 OPEN PORTS:")
            for port in sorted(self.open_ports):
                info = self.scan_results[port]
                print(f"  {port}/tcp - {info['service']} - {info['response_time']}ms")
        
        # Save to file
        self.save_to_file(target)
    
    def get_scan_duration(self):
        """Calculate total scan duration"""
        # Simplified - in real implementation, track start/end times
        return "N/A"
    
    def save_to_file(self, target):
        """Save results to file"""
        filename = f"scan_{target}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(filename, 'w') as f:
            f.write(f"Port Scan Report\n")
            f.write(f"Target: {target}\n")
            f.write(f"Date: {datetime.now()}\n")
            f.write(f"Open Ports: {len(self.open_ports)}\n\n")
            
            for port in sorted(self.open_ports):
                info = self.scan_results[port]
                f.write(f"{port}/tcp - {info['service']}\n")
        
        print(f"💾 Report saved to: {filename}")

def main():
    scanner = AdvancedPortScanner()
    
    print("🚀 CSR Advanced Port Scanner")
    print("=" * 40)
    
    target = input("Enter target (IP/hostname): ").strip()
    if not target:
        target = "scanme.nmap.org"  # Nmap's test service
    
    port_range = input("Enter port range (e.g., 1-1000): ").strip()
    if port_range and '-' in port_range:
        start, end = map(int, port_range.split('-'))
    else:
        start, end = 1, 1000
    
    print(f"\nStarting scan...")
    scanner.scan_range(target, start, end)

if __name__ == "__main__":
    main()
