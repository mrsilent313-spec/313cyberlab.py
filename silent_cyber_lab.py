#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════╗
║          SILENT CYBER LAB - OSINT & RECON TOOLKIT               ║
║          [ TEAM SILENT 313 ] :: OSINT & RECON TOOLKIT            ║
║          :: BUILD BY MR SILENT313 NASRU ::                       ║
╚══════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import socket
import hashlib
import base64
import json
import urllib.request
import urllib.parse
import subprocess
from datetime import datetime

# ─── Colors ──────────────────────────────────────────────────────
G = '\033[92m'   # Green
R = '\033[91m'   # Red
Y = '\033[93m'   # Yellow
B = '\033[94m'   # Blue
C = '\033[96m'   # Cyan
W = '\033[97m'   # White
D = '\033[90m'   # Dark Gray
RST = '\033[0m'  # Reset

# ─── Banner ──────────────────────────────────────────────────────
def banner():
    os.system('clear')
    print(f"""
{G}  ███████╗██╗██╗     ███████╗███╗   ██╗████████╗
  ██╔════╝██║██║     ██╔════╝████╗  ██║╚══██╔══╝
  ███████╗██║██║     █████╗  ██╔██╗ ██║   ██║   
  ╚════██║██║██║     ██╔══╝  ██║╚██╗██║   ██║   
  ███████║██║███████╗███████╗██║ ╚████║   ██║   
  ╚══════╝╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   {RST}
{G}           ██████╗██╗   ██╗██████╗ ███████╗██████╗ 
          ██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗
          ██║     ██║   ██║██████╔╝█████╗  ██████╔╝
          ██║     ██║   ██║██╔══██╗██╔══╝  ██╔══██╗
          ╚██████╗╚██████╔╝██║  ██║███████╗██║  ██║
           ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝{RST}
{C}  ═══════════════════════════════════════════════════{RST}
  {G}[ TEAM SILENT 313 ] :: OSINT & RECON TOOLKIT{RST}
  {Y}:: BUILD BY MR SILENT313 NASRU ::{RST}
  {C}═══════════════════════════════════════════════════{RST}
    """)

def status_bar():
    now = datetime.now().strftime("%I:%M:%S %p")
    print(f"{G}  [ SYSTEM ONLINE ]  {now}{RST}")
    print(f"{G}  [ 11 MODULES LOADED ]  [ NO KEYS REQUIRED ]{RST}")
    print(f"{C}  {'─' * 50}{RST}")

def menu():
    print(f"""
  {G}[ 1]{RST} IP LOOKUP
  {G}[ 2]{RST} CVE SEARCH
  {G}[ 3]{RST} SUBDOMAINS
  {G}[ 4]{RST} DNS LOOKUP
  {G}[ 5]{RST} WHOIS
  {G}[ 6]{RST} HASH GEN
  {G}[ 7]{RST} BASE64
  {G}[ 8]{RST} PASS CHECK
  {G}[ 9]{RST} QR CODE
  {G}[10]{RST} USERNAME
  {G}[11]{RST} PORT REF
  {R}[ 0]{RST} EXIT
    """)
    print(f"{G}  SELECT MODULE >> {RST}", end="")

# ─── Module 1: IP Lookup ───────────────────────────────────────
def ip_lookup():
    print(f"\n{C}[+] IP LOOKUP MODULE{RST}")
    ip = input(f"{Y}  Enter IP/Domain: {RST}").strip()
    if not ip:
        print(f"{R}  [!] Empty input!{RST}")
        return
    try:
        # Try to resolve domain to IP
        try:
            resolved_ip = socket.gethostbyname(ip)
            print(f"{G}  [+] Resolved IP: {resolved_ip}{RST}")
            ip = resolved_ip
        except:
            pass

        # Get IP info from ip-api.com
        url = f"http://ip-api.com/json/{ip}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())

        if data.get('status') == 'success':
            print(f"\n{G}  ═══ IP INFORMATION ═══{RST}")
            print(f"  {C}IP:{RST}        {data.get('query', 'N/A')}")
            print(f"  {C}Country:{RST}   {data.get('country', 'N/A')} ({data.get('countryCode', 'N/A')})")
            print(f"  {C}Region:{RST}    {data.get('regionName', 'N/A')}")
            print(f"  {C}City:{RST}      {data.get('city', 'N/A')}")
            print(f"  {C}ZIP:{RST}       {data.get('zip', 'N/A')}")
            print(f"  {C}Lat/Lon:{RST}   {data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}")
            print(f"  {C}Timezone:{RST}  {data.get('timezone', 'N/A')}")
            print(f"  {C}ISP:{RST}       {data.get('isp', 'N/A')}")
            print(f"  {C}Org:{RST}       {data.get('org', 'N/A')}")
            print(f"  {C}AS:{RST}        {data.get('as', 'N/A')}")
        else:
            print(f"{R}  [!] Could not fetch IP info!{RST}")
    except Exception as e:
        print(f"{R}  [!] Error: {e}{RST}")
    input(f"\n{Y}  Press Enter to continue...{RST}")

# ─── Module 2: CVE Search ──────────────────────────────────────
def cve_search():
    print(f"\n{C}[+] CVE SEARCH MODULE{RST}")
    query = input(f"{Y}  Enter CVE ID or Keyword (e.g., CVE-2021-44228): {RST}").strip()
    if not query:
        print(f"{R}  [!] Empty input!{RST}")
        return
    try:
        # Search via NVD API
        if query.upper().startswith("CVE-"):
            url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={query.upper()}"
        else:
            url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={urllib.parse.quote(query)}&resultsPerPage=5"

        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as response:
            data = json.loads(response.read().decode())

        vulnerabilities = data.get('vulnerabilities', [])
        if not vulnerabilities:
            print(f"{R}  [!] No CVE found!{RST}")
            return

        print(f"\n{G}  ═══ CVE RESULTS ═══{RST}")
        for i, vuln in enumerate(vulnerabilities[:5], 1):
            cve = vuln.get('cve', {})
            cve_id = cve.get('id', 'N/A')
            desc = cve.get('descriptions', [{}])[0].get('value', 'No description')
            metrics = cve.get('metrics', {})
            cvss = metrics.get('cvssMetricV31', [{}])[0].get('cvssData', {}).get('baseScore', 'N/A')
            severity = metrics.get('cvssMetricV31', [{}])[0].get('cvssData', {}).get('baseSeverity', 'N/A')

            print(f"\n  {Y}[{i}] {cve_id}{RST}")
            print(f"  {C}CVSS Score:{RST} {cvss} ({severity})")
            print(f"  {C}Description:{RST} {desc[:200]}...")

    except Exception as e:
        print(f"{R}  [!] Error: {e}{RST}")
    input(f"\n{Y}  Press Enter to continue...{RST}")

# ─── Module 3: Subdomains ──────────────────────────────────────
def subdomains():
    print(f"\n{C}[+] SUBDOMAIN ENUMERATION MODULE{RST}")
    domain = input(f"{Y}  Enter Domain (e.g., example.com): {RST}").strip()
    if not domain:
        print(f"{R}  [!] Empty input!{RST}")
        return

    # Common subdomains list
    common_subs = [
        'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'webdisk',
        'ns2', 'cpanel', 'whm', 'autodiscover', 'autoconfig', 'ns3', 'm', 'imap',
        'test', 'ns', 'blog', 'pop3', 'dev', 'www2', 'admin', 'forum', 'news',
        'vpn', 'ns4', 'email', 'webmaster', 'api', 'support', 'mobile', 'remote',
        'shop', 'portal', 'dns', 'www1', 'www3', 'dns1', 'dns2', 'mx', 'mx1',
        'mx2', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'ftp1', 'ftp2', 'ssh', 'git', 'cdn', 'cloud', 'app', 'secure', 'login',
        'web', 'static', 'media', 'files', 'img', 'images', 'video', 'videos',
        'docs', 'wiki', 'help', 'status', 'monitor', 'stats', 'analytics',
        'staging', 'beta', 'demo', 'try', 'go', 'start', 'home', 'main',
        'server', 'host', 'node', 'proxy', 'cache', 'edge', 'origin',
        'us', 'eu', 'asia', 'au', 'uk', 'ca', 'de', 'fr', 'jp', 'in',
        'pay', 'payment', 'billing', 'invoice', 'account', 'user', 'users',
        'member', 'members', 'client', 'clients', 'customer', 'customers',
        'partner', 'partners', 'vendor', 'vendors', 'supplier', 'suppliers',
        'career', 'careers', 'job', 'jobs', 'hire', 'join', 'team', 'about',
        'contact', 'contacts', 'info', 'press', 'media', 'newsroom',
        'event', 'events', 'conference', 'webinar', 'training', 'course',
        'learn', 'education', 'academy', 'school', 'university', 'college',
        'research', 'lab', 'labs', 'science', 'tech', 'technology',
        'dev', 'developer', 'developers', 'api', 'api1', 'api2', 'apis',
        'sdk', 'docs', 'documentation', 'reference', 'guide', 'tutorial',
        'community', 'forum', 'forums', 'discuss', 'discussion', 'chat',
        'social', 'share', 'connect', 'network', 'networks', 'group',
        'groups', 'club', 'clubs', 'hub', 'center', 'centre', 'zone',
        'area', 'region', 'district', 'sector', 'zone', 'park', 'square',
        'market', 'store', 'shop', 'mall', 'mart', 'bazaar', 'plaza',
        'trade', 'trading', 'exchange', 'marketplace', 'auction',
        'sale', 'sales', 'promo', 'promotion', 'deal', 'deals', 'offer',
        'offers', 'discount', 'coupon', 'voucher', 'gift', 'rewards',
        'loyalty', 'program', 'programs', 'campaign', 'campaigns',
        'ad', 'ads', 'advert', 'advertising', 'marketing', 'brand',
        'brands', 'product', 'products', 'service', 'services',
        'solution', 'solutions', 'platform', 'system', 'tool', 'tools',
        'resource', 'resources', 'asset', 'assets', 'library', 'lib',
        'repo', 'repository', 'source', 'code', 'build', 'ci', 'cd',
        'pipeline', 'deploy', 'deployment', 'release', 'releases',
        'version', 'versions', 'update', 'updates', 'patch', 'patches',
        'fix', 'fixes', 'bug', 'bugs', 'issue', 'issues', 'ticket',
        'tickets', 'support', 'helpdesk', 'service', 'services',
        'desk', 'assist', 'assistance', 'care', 'help', 'faq', 'faqs',
        'kb', 'knowledge', 'wiki', 'glossary', 'dictionary', 'index',
        'search', 'find', 'lookup', 'query', 'browse', 'explorer',
        'navigator', 'map', 'maps', 'location', 'locations', 'place',
        'places', 'address', 'addresses', 'direction', 'directions',
        'route', 'routes', 'path', 'paths', 'way', 'ways', 'track',
        'tracking', 'trace', 'traceroute', 'ping', 'probe', 'scan',
        'scanner', 'security', 'sec', 'safe', 'safety', 'protect',
        'protection', 'guard', 'shield', 'defense', 'defence', 'firewall',
        'waf', 'ids', 'ips', 'siem', 'soc', 'noc', 'ops', 'operations',
        'admin', 'administrator', 'root', 'superuser', 'sudo', 'su',
        'panel', 'dashboard', 'control', 'manage', 'management', 'manager',
        'config', 'configuration', 'settings', 'preference', 'preferences',
        'option', 'options', 'setup', 'install', 'installer', 'setup',
        'wizard', 'guide', 'assistant', 'bot', 'robot', 'ai', 'ml',
        'machine', 'learning', 'deep', 'neural', 'network', 'algo',
        'algorithm', 'compute', 'computing', 'cloud', 'serverless',
        'container', 'docker', 'kubernetes', 'k8s', 'cluster', 'node',
        'worker', 'master', 'slave', 'replica', 'backup', 'restore',
        'snapshot', 'archive', 'archives', 'history', 'log', 'logs',
        'logging', 'audit', 'audits', 'report', 'reports', 'reporting',
        'analytics', 'metric', 'metrics', 'monitor', 'monitoring',
        'observe', 'observability', 'trace', 'tracing', 'telemetry',
        'data', 'database', 'db', 'sql', 'mysql', 'postgres', 'mongo',
        'redis', 'cache', 'caching', 'queue', 'queues', 'message',
        'messaging', 'pubsub', 'pub', 'sub', 'stream', 'streaming',
        'event', 'events', 'eventing', 'bus', 'kafka', 'rabbitmq',
        'mq', 'broker', 'gateway', 'ingress', 'egress', 'loadbalancer',
        'lb', 'balancer', 'vip', 'virtual', 'floating', 'elastic',
        'auto', 'auto-scaling', 'scaling', 'scale', 'resize', 'upgrade',
        'downgrade', 'migrate', 'migration', 'transfer', 'sync',
        'synchronize', 'replicate', 'replication', 'mirror', 'clone',
        'copy', 'backup', 'snapshot', 'checkpoint', 'save', 'export',
        'import', 'upload', 'download', 'transfer', 'move', 'copy',
        'share', 'shared', 'public', 'private', 'internal', 'external',
        'dmz', 'intranet', 'extranet', 'lan', 'wan', 'man', 'san',
        'nas', 'storage', 'store', 'disk', 'volume', 'drive', 'raid',
        'array', 'pool', 'bucket', 'object', 'objectstore', 's3',
        'blob', 'file', 'files', 'filestore', 'filesystem', 'fs',
        'mount', 'mounts', 'nfs', 'smb', 'cifs', 'afs', 'ftp', 'sftp',
        'scp', 'rsync', 'transfer', 'xfer', 'uploads', 'downloads',
        'assets', 'static', 'css', 'js', 'javascript', 'script',
        'scripts', 'style', 'styles', 'stylesheet', 'stylesheets',
        'font', 'fonts', 'icon', 'icons', 'image', 'images', 'img',
        'picture', 'pictures', 'photo', 'photos', 'gallery', 'album',
        'media', 'video', 'videos', 'movie', 'movies', 'film', 'films',
        'clip', 'clips', 'stream', 'streams', 'live', 'livestream',
        'broadcast', 'cast', 'podcast', 'radio', 'tv', 'television',
        'channel', 'channels', 'program', 'programs', 'show', 'shows',
        'episode', 'episodes', 'series', 'season', 'seasons', 'content',
        'contents', 'article', 'articles', 'post', 'posts', 'blog',
        'blogs', 'story', 'stories', 'news', 'headline', 'headlines',
        'breaking', 'update', 'updates', 'alert', 'alerts', 'notify',
        'notification', 'notifications', 'reminder', 'reminders',
        'message', 'messages', 'msg', 'msgs', 'chat', 'chats',
        'conversation', 'conversations', 'thread', 'threads', 'reply',
        'replies', 'comment', 'comments', 'review', 'reviews', 'rating',
        'ratings', 'feedback', 'survey', 'surveys', 'poll', 'polls',
        'vote', 'votes', 'voting', 'election', 'ballot', 'referendum',
        'petition', 'petitions', 'cause', 'causes', 'campaign',
        'campaigns', 'movement', 'movements', 'activism', 'protest',
        'rally', 'rallies', 'march', 'marches', 'demonstration',
        'demonstrations', 'strike', 'strikes', 'boycott', 'boycotts',
        'embargo', 'sanction', 'sanctions', 'blockade', 'blockades',
        'barrier', 'barriers', 'wall', 'walls', 'fence', 'fences',
        'gate', 'gates', 'door', 'doors', 'portal', 'portals',
        'entry', 'entries', 'exit', 'exits', 'access', 'accesses',
        'entrance', 'entrances', 'ingress', 'ingresses', 'egress',
        'egresses', 'inlet', 'inlets', 'outlet', 'outlets', 'vent',
        'vents', 'ventilation', 'air', 'fan', 'fans', 'cooler',
        'coolers', 'ac', 'hvac', 'climate', 'temp', 'temperature',
        'humidity', 'pressure', 'barometer', 'weather', 'forecast',
        'prediction', 'predictions', 'model', 'models', 'simulation',
        'simulations', 'emulation', 'emulations', 'virtual', 'virtualization',
        'vm', 'vms', 'guest', 'guests', 'host', 'hosts', 'hypervisor',
        'kvm', 'xen', 'vmware', 'virtualbox', 'vbox', 'parallels',
        'qemu', 'proxmox', 'esxi', 'vsphere', 'vcenter', 'vcloud',
        'openstack', 'cloudstack', 'eucalyptus', 'opennebula', 'ovirt',
        'rhev', 'rhv', 'satellite', 'foreman', 'puppet', 'chef',
        'ansible', 'salt', 'terraform', 'vagrant', 'packer', 'vault',
        'consul', 'nomad', 'boundary', 'waypoint', 'nomad', 'consul',
        'vault', 'terraform', 'packer', 'vagrant', 'boundary',
        'waypoint', 'nomad', 'consul', 'vault', 'terraform', 'packer'
    ]

    print(f"\n{Y}  Scanning subdomains for: {domain}{RST}")
    print(f"{D}  This may take a while...{RST}\n")

    found = []
    count = 0
    total = len(common_subs)

    for sub in common_subs:
        count += 1
        if count % 50 == 0:
            print(f"{D}  Progress: {count}/{total}...{RST}", end='\r')

        full_domain = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(full_domain)
            found.append((full_domain, ip))
            print(f"  {G}[+] {full_domain:<30} => {ip}{RST}")
        except socket.gaierror:
            pass
        except Exception:
            pass

    print(f"\n{G}  [+] Found {len(found)} subdomains{RST}")
    input(f"\n{Y}  Press Enter to continue...{RST}")

# ─── Module 4: DNS Lookup ──────────────────────────────────────
def dns_lookup():
    print(f"\n{C}[+] DNS LOOKUP MODULE{RST}")
    domain = input(f"{Y}  Enter Domain: {RST}").strip()
    if not domain:
        print(f"{R}  [!] Empty input!{RST}")
        return
    try:
        print(f"\n{G}  ═══ DNS RECORDS FOR {domain} ═══{RST}")

        # A Record
        try:
            result = socket.gethostbyname_ex(domain)
            print(f"\n  {C}A Records:{RST}")
            for ip in result[2]:
                print(f"    {ip}")
        except:
            print(f"  {R}  No A records found{RST}")

        # MX Records (using dig if available)
        try:
            result = subprocess.run(['dig', '+short', 'MX', domain], 
                                  capture_output=True, text=True, timeout=5)
            if result.stdout.strip():
                print(f"\n  {C}MX Records:{RST}")
                for line in result.stdout.strip().split('\n'):
                    if line:
                        print(f"    {line}")
        except:
            pass

        # NS Records
        try:
            result = subprocess.run(['dig', '+short', 'NS', domain], 
                                  capture_output=True, text=True, timeout=5)
            if result.stdout.strip():
                print(f"\n  {C}NS Records:{RST}")
                for line in result.stdout.strip().split('\n'):
                    if line:
                        print(f"    {line}")
        except:
            pass

        # TXT Records
        try:
            result = subprocess.run(['dig', '+short', 'TXT', domain], 
                                  capture_output=True, text=True, timeout=5)
            if result.stdout.strip():
                print(f"\n  {C}TXT Records:{RST}")
                for line in result.stdout.strip().split('\n'):
                    if line:
                        print(f"    {line}")
        except:
            pass

    except Exception as e:
        print(f"{R}  [!] Error: {e}{RST}")
    input(f"\n{Y}  Press Enter to continue...{RST}")

# ─── Module 5: WHOIS ───────────────────────────────────────────
def whois_lookup():
    print(f"\n{C}[+] WHOIS LOOKUP MODULE{RST}")
    domain = input(f"{Y}  Enter Domain: {RST}").strip()
    if not domain:
        print(f"{R}  [!] Empty input!{RST}")
        return
    try:
        result = subprocess.run(['whois', domain], capture_output=True, text=True, timeout=10)
        if result.stdout:
            print(f"\n{G}  ═══ WHOIS INFORMATION ═══{RST}")
            lines = result.stdout.split('\n')
            for line in lines[:50]:  # Show first 50 lines
                if line.strip() and not line.startswith('%'):
                    print(f"  {line}")
            if len(lines) > 50:
                print(f"\n  {D}... ({len(lines) - 50} more lines) ...{RST}")
        else:
            print(f"{R}  [!] No WHOIS data found{RST}")
    except FileNotFoundError:
        print(f"{R}  [!] whois command not found. Install with: pkg install whois{RST}")
    except Exception as e:
        print(f"{R}  [!] Error: {e}{RST}")
    input(f"\n{Y}  Press Enter to continue...{RST}")

# ─── Module 6: Hash Generator ──────────────────────────────────
def hash_gen():
    print(f"\n{C}[+] HASH GENERATOR MODULE{RST}")
    text = input(f"{Y}  Enter text to hash: {RST}").strip()
    if not text:
        print(f"{R}  [!] Empty input!{RST}")
        return

    print(f"\n{G}  ═══ HASHES ═══{RST}")
    print(f"  {C}MD5:{RST}    {hashlib.md5(text.encode()).hexdigest()}")
    print(f"  {C}SHA1:{RST}   {hashlib.sha1(text.encode()).hexdigest()}")
    print(f"  {C}SHA224:{RST} {hashlib.sha224(text.encode()).hexdigest()}")
    print(f"  {C}SHA256:{RST} {hashlib.sha256(text.encode()).hexdigest()}")
    print(f"  {C}SHA384:{RST} {hashlib.sha384(text.encode()).hexdigest()}")
    print(f"  {C}SHA512:{RST} {hashlib.sha512(text.encode()).hexdigest()}")
    print(f"  {C}BLAKE2b:{RST} {hashlib.blake2b(text.encode()).hexdigest()}")

    input(f"\n{Y}  Press Enter to continue...{RST}")

# ─── Module 7: Base64 ────────────────────────────────────────────
def base64_tool():
    print(f"\n{C}[+] BASE64 ENCODE/DECODE MODULE{RST}")
    print(f"  {Y}[1] Encode{RST}")
    print(f"  {Y}[2] Decode{RST}")
    choice = input(f"\n{G}  Select option: {RST}").strip()

    if choice == '1':
        text = input(f"{Y}  Enter text to encode: {RST}").strip()
        if text:
            encoded = base64.b64encode(text.encode()).decode()
            print(f"\n{G}  [+] Encoded:{RST} {encoded}")
        else:
            print(f"{R}  [!] Empty input!{RST}")
    elif choice == '2':
        text = input(f"{Y}  Enter Base64 to decode: {RST}").strip()
        try:
            decoded = base64.b64decode(text).decode()
            print(f"\n{G}  [+] Decoded:{RST} {decoded}")
        except:
            print(f"{R}  [!] Invalid Base64!{RST}")
    else:
        print(f"{R}  [!] Invalid option!{RST}")

    input(f"\n{Y}  Press Enter to continue...{RST}")

# ─── Module 8: Password Check ──────────────────────────────────
def pass_check():
    print(f"\n{C}[+] PASSWORD STRENGTH CHECKER{RST}")
    password = input(f"{Y}  Enter password: {RST}").strip()
    if not password:
        print(f"{R}  [!] Empty input!{RST}")
        return

    score = 0
    checks = []

    if len(password) >= 8:
        score += 1
        checks.append(f"{G}✓ Length >= 8{RST}")
    else:
        checks.append(f"{R}✗ Length < 8{RST}")

    if any(c.isupper() for c in password):
        score += 1
        checks.append(f"{G}✓ Uppercase{RST}")
    else:
        checks.append(f"{R}✗ No Uppercase{RST}")

    if any(c.islower() for c in password):
        score += 1
        checks.append(f"{G}✓ Lowercase{RST}")
    else:
        checks.append(f"{R}✗ No Lowercase{RST}")

    if any(c.isdigit() for c in password):
        score += 1
        checks.append(f"{G}✓ Numbers{RST}")
    else:
        checks.append(f"{R}✗ No Numbers{RST}")

    if any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password):
        score += 1
        checks.append(f"{G}✓ Special Chars{RST}")
    else:
        checks.append(f"{R}✗ No Special Chars{RST}")

    print(f"\n{G}  ═══ PASSWORD ANALYSIS ═══{RST}")
    for check in checks:
        print(f"  {check}")

    # Calculate entropy
    import math
    charset = 0
    if any(c.islower() for c in password): charset += 26
    if any(c.isupper() for c in password): charset += 26
    if any(c.isdigit() for c in password): charset += 10
    if any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password): charset += 32

    if charset > 0:
        entropy = len(password) * math.log2(charset)
        print(f"\n  {C}Entropy:{RST} {entropy:.2f} bits")
        print(f"  {C}Score:{RST} {score}/5")

        if score <= 2:
            print(f"\n  {R}[!] WEAK PASSWORD{RST}")
        elif score == 3:
            print(f"\n  {Y}[!] MODERATE PASSWORD{RST}")
        elif score >= 4:
            print(f"\n  {G}[+] STRONG PASSWORD{RST}")

    # Generate hash for reference
    print(f"\n  {C}SHA256 Hash:{RST} {hashlib.sha256(password.encode()).hexdigest()}")

    input(f"\n{Y}  Press Enter to continue...{RST}")

# ─── Module 9: QR Code ─────────────────────────────────────────
def qr_code():
    print(f"\n{C}[+] QR CODE GENERATOR{RST}")
    text = input(f"{Y}  Enter text/URL for QR: {RST}").strip()
    if not text:
        print(f"{R}  [!] Empty input!{RST}")
        return

    try:
        import qrcode
        qr = qrcode.QRCode(version=1, box_size=2, border=2)
        qr.add_data(text)
        qr.make(fit=True)

        # Print ASCII QR
        print(f"\n{G}  ═══ QR CODE (ASCII) ═══{RST}\n")
        qr.print_ascii(invert=True)
        print(f"\n  {C}Data:{RST} {text}")

        # Save to file
        save = input(f"\n{Y}  Save as PNG? (y/n): {RST}").strip().lower()
        if save == 'y':
            filename = input(f"{Y}  Filename (default: qr.png): {RST}").strip() or "qr.png"
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(filename)
            print(f"{G}  [+] Saved as {filename}{RST}")
    except ImportError:
        print(f"{R}  [!] qrcode module not found!{RST}")
        print(f"{Y}  Install with: pip install qrcode[pil]{RST}")

        # Fallback: Generate a simple text-based representation
        print(f"\n{G}  ═══ TEXT REPRESENTATION ═══{RST}")
        print(f"  {C}Data:{RST} {text}")
        print(f"  {C}Base64:{RST} {base64.b64encode(text.encode()).decode()}")
        print(f"  {C}SHA256:{RST} {hashlib.sha256(text.encode()).hexdigest()}")

    input(f"\n{Y}  Press Enter to continue...{RST}")

# ─── Module 10: Username OSINT ─────────────────────────────────
def username_osint():
    print(f"\n{C}[+] USERNAME OSINT MODULE{RST}")
    username = input(f"{Y}  Enter username to check: {RST}").strip()
    if not username:
        print(f"{R}  [!] Empty input!{RST}")
        return

    print(f"\n{G}  ═══ CHECKING USERNAME: {username} ═══{RST}\n")

    # List of platforms to check
    platforms = {
        'GitHub': f'https://github.com/{username}',
        'Twitter/X': f'https://x.com/{username}',
        'Instagram': f'https://instagram.com/{username}',
        'Reddit': f'https://reddit.com/user/{username}',
        'YouTube': f'https://youtube.com/@{username}',
        'TikTok': f'https://tiktok.com/@{username}',
        'Facebook': f'https://facebook.com/{username}',
        'LinkedIn': f'https://linkedin.com/in/{username}',
        'Pinterest': f'https://pinterest.com/{username}',
        'Twitch': f'https://twitch.tv/{username}',
        'Steam': f'https://steamcommunity.com/id/{username}',
        'Spotify': f'https://open.spotify.com/user/{username}',
        'Medium': f'https://medium.com/@{username}',
        'Dev.to': f'https://dev.to/{username}',
        'GitLab': f'https://gitlab.com/{username}',
        'Bitbucket': f'https://bitbucket.org/{username}',
        'HackerNews': f'https://news.ycombinator.com/user?id={username}',
        'ProductHunt': f'https://producthunt.com/@{username}',
        'Quora': f'https://quora.com/profile/{username}',
        'Vimeo': f'https://vimeo.com/{username}',
        'SoundCloud': f'https://soundcloud.com/{username}',
        'Flickr': f'https://flickr.com/people/{username}',
        'Tumblr': f'https://{username}.tumblr.com',
        'Mastodon': f'https://mastodon.social/@{username}',
        'Keybase': f'https://keybase.io/{username}',
        'Pastebin': f'https://pastebin.com/u/{username}',
        'Replit': f'https://replit.com/@{username}',
        'CodePen': f'https://codepen.io/{username}',
        'StackOverflow': f'https://stackoverflow.com/users/{username}',
        'TryHackMe': f'https://tryhackme.com/p/{username}',
        'HackTheBox': f'https://app.hackthebox.com/users/{username}',
    }

    found_count = 0
    for platform, url in platforms.items():
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            req.get_method = lambda: 'HEAD'
            try:
                response = urllib.request.urlopen(req, timeout=5)
                if response.getcode() == 200:
                    print(f"  {G}[+] {platform:<20} => {url}{RST}")
                    found_count += 1
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    print(f"  {R}[-] {platform:<20} => Not Found{RST}")
                else:
                    print(f"  {Y}[?] {platform:<20} => Status: {e.code}{RST}")
            except Exception:
                print(f"  {D}[?] {platform:<20} => Check manually{RST}")
        except Exception:
            print(f"  {D}[?] {platform:<20} => Error{RST}")

    print(f"\n{G}  [+] Found on {found_count} platforms{RST}")
    input(f"\n{Y}  Press Enter to continue...{RST}")

# ─── Module 11: Port Reference ─────────────────────────────────
def port_ref():
    print(f"\n{C}[+] PORT REFERENCE MODULE{RST}")

    port_db = {
        20: 'FTP Data', 21: 'FTP Control', 22: 'SSH', 23: 'Telnet',
        25: 'SMTP', 53: 'DNS', 67: 'DHCP Server', 68: 'DHCP Client',
        69: 'TFTP', 80: 'HTTP', 88: 'Kerberos', 110: 'POP3',
        111: 'RPCbind', 113: 'Ident', 119: 'NNTP', 123: 'NTP',
        135: 'MS RPC', 137: 'NetBIOS Name', 138: 'NetBIOS Datagram',
        139: 'NetBIOS Session', 143: 'IMAP', 161: 'SNMP',
        162: 'SNMP Trap', 179: 'BGP', 194: 'IRC', 201: 'AppleTalk',
        264: 'BGMP', 318: 'TSP', 381: 'HP OpenView', 383: 'HP OpenView',
        389: 'LDAP', 411: 'Direct Connect', 412: 'Direct Connect',
        443: 'HTTPS', 445: 'SMB', 464: 'Kerberos Change/Set',
        465: 'SMTPS', 497: 'Retrospect', 500: 'ISAKMP', 512: 'rexec',
        513: 'rlogin', 514: 'syslog', 515: 'LPD/LPR', 520: 'RIP',
        521: 'RIPng', 540: 'UUCP', 554: 'RTSP', 546: 'DHCPv6 Client',
        547: 'DHCPv6 Server', 560: 'rmonitor', 563: 'NNTP over SSL',
        587: 'SMTP Submission', 591: 'FileMaker', 593: 'MS DCOM',
        631: 'IPP', 636: 'LDAPS', 639: 'MSDP', 646: 'LDP',
        691: 'MS Exchange', 860: 'iSCSI', 873: 'rsync', 902: 'VMware',
        903: 'VMware', 989: 'FTPS Data', 990: 'FTPS Control',
        993: 'IMAPS', 995: 'POP3S', 1025: 'MS RPC', 1026: 'Windows Messenger',
        1027: 'Windows Messenger', 1028: 'Windows Messenger',
        1029: 'Windows Messenger', 1080: 'SOCKS Proxy',
        1194: 'OpenVPN', 1214: 'Kazaa', 1241: 'Nessus',
        1311: 'Dell OpenManage', 1337: 'WASTE/Elite', 1433: 'MS SQL',
        1434: 'MS SQL Monitor', 1512: 'WINS', 1589: 'Cisco VQP',
        1701: 'L2TP', 1723: 'PPTP', 1725: 'Steam', 1755: 'MMS',
        1812: 'RADIUS', 1813: 'RADIUS Accounting', 1863: 'MSN',
        1900: 'UPnP', 1985: 'HSRP', 2000: 'Cisco SCCP', 2002: 'Cisco ACS',
        2049: 'NFS', 2082: 'cPanel', 2083: 'cPanel SSL', 2100: 'Oracle XDB',
        2222: 'DirectAdmin', 2302: 'Halo', 2483: 'Oracle DB SSL',
        2484: 'Oracle DB SSL', 2745: 'Bagle.C', 2967: 'Symantec AV',
        3050: 'Interbase', 3074: 'Xbox Live', 3124: 'HTTP Proxy',
        3127: 'MyDoom', 3128: 'HTTP Proxy', 3222: 'GLBP', 3260: 'iSCSI Target',
        3306: 'MySQL', 3389: 'RDP', 3689: 'DAAP', 3690: 'SVN',
        3724: 'World of Warcraft', 3784: 'Ventrilo', 3785: 'Ventrilo',
        4333: 'mSQL', 4444: 'Blaster', 4664: 'Google Desktop',
        4672: 'eMule', 4899: 'Radmin', 5000: 'UPnP', 5001: 'iperf',
        5004: 'RTP', 5005: 'RTCP', 5050: 'Yahoo Messenger',
        5060: 'SIP', 5061: 'SIP-TLS', 5190: 'AIM/ICQ', 5222: 'XMPP',
        5223: 'XMPP SSL', 5228: 'Android Market', 5432: 'PostgreSQL',
        5500: 'VNC Server', 5554: 'Sasser', 5631: 'pcAnywhere',
        5632: 'pcAnywhere', 5800: 'VNC Web', 5900: 'VNC',
        6000: 'X11', 6001: 'X11', 6112: 'Battle.net', 6129: 'DameWare',
        6257: 'WinMX', 6346: 'Gnutella', 6347: 'Gnutella',
        6500: 'GameSpy Arcade', 6566: 'SANE', 6588: 'AnalogX Proxy',
        6665: 'IRC', 6666: 'IRC', 6667: 'IRC', 6668: 'IRC', 6669: 'IRC',
        6679: 'IRC SSL', 6697: 'IRC SSL', 6699: 'Napster',
        6881: 'BitTorrent', 6882: 'BitTorrent', 6883: 'BitTorrent',
        6884: 'BitTorrent', 6885: 'BitTorrent', 6886: 'BitTorrent',
        6887: 'BitTorrent', 6888: 'BitTorrent', 6889: 'BitTorrent',
        6890: 'BitTorrent', 6901: 'Windows Messenger', 6970: 'QuickTime',
        7212: 'GhostSurf', 7648: 'CU-SeeMe', 7649: 'CU-SeeMe',
        8000: 'iRDMI', 8008: 'HTTP Alt', 8080: 'HTTP Proxy',
        8086: 'Kaspersky AV', 8087: 'Kaspersky AV', 8118: 'Privoxy',
        8200: 'VMware Server', 8443: 'HTTPS Alt', 8500: 'Adobe ColdFusion',
        8767: 'TeamSpeak', 8866: 'Bagle.B', 9100: 'RAW Print',
        9119: 'MXit', 9800: 'WebDAV', 9898: 'Dabber', 9988: 'Rbot/Spybot',
        9999: 'Urchin', 10000: 'Webmin', 10113: 'NetIQ Endpoint',
        10114: 'NetIQ Endpoint', 10115: 'NetIQ Endpoint',
        10116: 'NetIQ Endpoint', 11371: 'OpenPGP Keyserver',
        12035: 'Second Life', 12345: 'NetBus', 13720: 'NetBackup',
        13721: 'NetBackup', 14567: 'Battlefield', 15118: 'Dipnet/Oddbob',
        19226: 'AdminSecure', 19638: 'Ensim', 20000: 'Usermin',
        24800: 'Synergy', 25999: 'Xfire', 27015: 'Half-Life',
        27017: 'MongoDB', 27374: 'Sub7', 28960: 'Call of Duty',
        31337: 'Back Orifice', 33434: 'traceroute',
    }

    choice = input(f"{Y}  [1] Search by Port Number\n  [2] Search by Service Name\n  Select: {RST}").strip()

    if choice == '1':
        port_input = input(f"{Y}  Enter port number: {RST}").strip()
        try:
            port = int(port_input)
            if port in port_db:
                print(f"\n  {G}[+] Port {port}: {port_db[port]}{RST}")
            else:
                print(f"\n  {Y}[?] Port {port}: Unknown/Custom{RST}")
        except ValueError:
            print(f"{R}  [!] Invalid port number!{RST}")

    elif choice == '2':
        service = input(f"{Y}  Enter service name (partial match): {RST}").strip().lower()
        matches = [(p, s) for p, s in port_db.items() if service in s.lower()]

        if matches:
            print(f"\n  {G}  ═══ MATCHING SERVICES ═══{RST}")
            for port, svc in matches[:20]:
                print(f"  {C}{port:<6}{RST} => {svc}")
            if len(matches) > 20:
                print(f"  {D}... and {len(matches) - 20} more ...{RST}")
        else:
            print(f"\n  {R}  [!] No matches found{RST}")

    else:
        print(f"{R}  [!] Invalid option!{RST}")

    input(f"\n{Y}  Press Enter to continue...{RST}")

# ─── Main ──────────────────────────────────────────────────────
def main():
    while True:
        banner()
        status_bar()
        menu()

        try:
            choice = input().strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\n{R}\n  [+] Exiting...{RST}")
            sys.exit(0)

        if choice == '0':
            print(f"\n{G}  [+] Thank you for using SILENT CYBER LAB!{RST}")
            print(f"  {Y}  Built by MR SILENT313 NASRU{RST}")
            print(f"  {C}  TEAM SILENT 313{RST}\n")
            sys.exit(0)
        elif choice == '1':
            ip_lookup()
        elif choice == '2':
            cve_search()
        elif choice == '3':
            subdomains()
        elif choice == '4':
            dns_lookup()
        elif choice == '5':
            whois_lookup()
        elif choice == '6':
            hash_gen()
        elif choice == '7':
            base64_tool()
        elif choice == '8':
            pass_check()
        elif choice == '9':
            qr_code()
        elif choice == '10':
            username_osint()
        elif choice == '11':
            port_ref()
        else:
            print(f"\n{R}  [!] Invalid option!{RST}")
            time.sleep(1)

if __name__ == '__main__':
    main()
