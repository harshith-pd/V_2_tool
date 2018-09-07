ENCRYPTED = "encrypted"
NOT_A_ZIP = "not a zip file"
CORRUPT = "corrupt"
SUCCESS = "SUCCESS"

#APKTOOL folder names
ASSETS_FOLDER = "assets"
RES_FOLDER = "res"
ANDROID_MANIFEST = "AndroidManifest"
SMALI_FOLDER = "smali"
LIB_FOLDER = "lib"
PERMISSIONS_ANDROID_MANIFEST = "permissions"
ORIGINAL_FOLDER = "original"

#Verification items for the signing info
DEBUG_SIGNATURE = "CN=Android Debug"

#Verification items for manifest xml
ANDROID_DEBUGGABLE_KEY = "android_debuggable"
ANDROID_ALLOW_BACKUP_KEY = "android_allow_backup"
ANDROID_FULL_BACKUP_CONTENT_KEY = "android_full_backup"
ANDROID_EXPORTED_KEY = "android_exported"
ANDROID_PROTECTION_LEVEL_KEY = "android_protection_level"
ANDROID_PROTECTION_VALUE_SIGNATURE = "signature"

#Verification items for re/xml
ALLOW_INTENT_HTTP = "http://*/*"
ALLOW_INTENT_HTTPS = "https://*/*"
ALLOW_INTENT_NAVIGATION = "http://*/*"
ACCESS_ORIGIN = "*"

ACCESS_ORIGIN_KEY = 'access_origin'
ALLOW_INTENT_KEY = 'allow_intent'
ALLOW_INTENT_NAVIGATION_KEY = 'allow_navigation'

#Application components from manifest file
SERVICE = "service"
ACTIVITY = "activity"
PROVIDER = "provider"
RECEIVER = "receiver"

#Info plist Constants
#url schemes
BUNDLE_URL_TYPES_KEY = "CFBundleURLTypes"
BUNDLE_TYPE_ROLE_KEY = "CFBundleTypeRole"
URL_SCHEME_NAMES_KEY = "CFBundleURLSchemes"
APP_TRANSPORT_SECURITY_KEY = "NSAppTransportSecurity"
EXCEPTION_DOMAINS_KEY = "NSExceptionDomains"
#ATS
APP_TRANSPORT_SECURITY_EXPECTED_VALUES = {"NSAllowsArbitraryLoads":False,
                                        "NSAllowsArbitraryLoadsForMedia":False,
                                        "NSAllowsArbitraryLoadsInWebContent":False,
                                        "NSAllowsLocalNetworking":False,
                                        "NSIncludesSubdomains":False,
                                        "NSExceptionAllowsInsecureHTTPLoads":False,
                                        "NSExceptionMinimumTLSVersion":"TLSv1.2 or above",
                                        "NSExceptionRequiresForwardSecrecy":True,
                                        "NSRequiresCertificateTransparency":False,
                                        "NSExceptionDomains":""}
#Execution constants
#values
PASS = "PASS"
FAIL = "FAIL"
#Security Threat levelname
SEVERE = "Severe"
MEDIUM = "Medium"
LOW = "Low"

STATUS = "test_result"
EXECUTION_OUTPUT = "test_findings"
PDF_LIST =['pdf_related_files/firstpage.pdf', 'pdf_related_files/confidentiality.pdf','pdf_related_files/reportSummary.pdf',
                'pdf_related_files/assessment_details.pdf', 'pdf_related_files/glossary.pdf']
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
########################################## 
APP_NAME = "com.ibm.android.analyzer.test"

INPUT_FOLDER = "/Users/digitalsecurity/.jenkins/workspace/test/test_run/com.ibm.android.analyzer.test/09_06_2018_17_42_29/input"

APKTOOL_OUTPUT_FOLDER = "/Users/digitalsecurity/.jenkins/workspace/test/test_run/com.ibm.android.analyzer.test/09_06_2018_17_42_29/output/apktool"

ENJARIFY_OUTPUT_FOLDER = "/Users/digitalsecurity/.jenkins/workspace/test/test_run/com.ibm.android.analyzer.test/09_06_2018_17_42_29/output/enjarify"

LOGS_FOLDER = "/Users/digitalsecurity/.jenkins/workspace/test/test_run/com.ibm.android.analyzer.test/09_06_2018_17_42_29/logs"

REPORT_FOLDER = "/Users/digitalsecurity/.jenkins/workspace/test/test_run/com.ibm.android.analyzer.test/09_06_2018_17_42_29/report"

CONFIG_FOLDER = "/Users/digitalsecurity/.jenkins/workspace/test/test_run/com.ibm.android.analyzer.test/09_06_2018_17_42_29/config"

TEST_RUN_FOLDER = "/Users/digitalsecurity/.jenkins/workspace/test/test_run"

CONFIG_ROOT_FOLDER = "/Users/digitalsecurity/.jenkins/workspace/test/config"

SCRIPTS_FOLDER = "/Users/digitalsecurity/.jenkins/workspace/test/Scripts"

TOOLS_FOLDER = "/Users/digitalsecurity/.jenkins/workspace/test/Tools"

TMP_FOLDER = "/Users/digitalsecurity/.jenkins/workspace/test/.tmp"
ROOT_FOLDER = '/Users/digitalsecurity/.jenkins/workspace/test'
