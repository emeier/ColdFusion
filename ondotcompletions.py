import sublime
import sublime_plugin

# http://livedocs.adobe.com/coldfusion/8/htmldocs/help.html?content=Expressions_7.html
completions = []
dotcompletions = {}
dotcompletions["cfcatch"] = [
    ("type", "type"),
    ("message", "message"),
    ("detail", "detail"),
    ("errNumber", "errNumber"),
    ("NativeErrorCode", "NativeErrorCode"),
    ("SQLState", "SQLState"),
    ("LockName", "LockName"),
    ("LockOperation", "LockOperation"),
    ("MissingFileName", "MissingFileName"),
    ("TagContext", "TagContext"),
    ("ErrorCode", "ErrorCode"),
    ("ExtendedInfo", "ExtendedInfo")
]
dotcompletions["cgi"] = [
    ("auth_password", "auth_password"),
    ("auth_type", "auth_type"),
    ("auth_user", "auth_user"),
    ("cert_cookie", "cert_cookie"),
    ("cert_flags", "cert_flags"),
    ("cert_issuer", "cert_issuer"),
    ("cert_keysize", "cert_keysize"),
    ("cert_secretkeysize", "cert_secretkeysize"),
    ("cert_serialnumber", "cert_serialnumber"),
    ("cert_server_issuer", "cert_server_issuer"),
    ("cert_server_subject", "cert_server_subject"),
    ("cert_subject", "cert_subject"),
    ("cf_template_path", "cf_template_path"),
    ("content_length", "content_length"),
    ("content_type", "content_type"),
    ("gateway_interface", "gateway_interface"),
    ("http_accept", "http_accept"),
    ("http_accept_encoding", "http_accept_encoding"),
    ("http_accept_language", "http_accept_language"),
    ("http_connection", "http_connection"),
    ("http_cookie", "http_cookie"),
    ("http_host", "http_host"),
    ("http_user_agent", "http_user_agent"),
    ("http_referer", "http_referer"),
    ("https", "https"),
    ("https_keysize", "https_keysize"),
    ("https_secretkeysize", "https_secretkeysize"),
    ("https_server_issuer", "https_server_issuer"),
    ("https_server_subject", "https_server_subject"),
    ("path_info", "path_info"),
    ("path_translated", "path_translated"),
    ("query_string", "query_string"),
    ("remote_addr", "remote_addr"),
    ("remote_host", "remote_host"),
    ("remote_user", "remote_user"),
    ("request_method", "request_method"),
    ("script_name", "script_name"),
    ("server_name", "server_name"),
    ("server_port", "server_port"),
    ("server_port_secure", "server_port_secure"),
    ("server_protocol", "server_protocol"),
    ("server_software", "server_software"),
    ("web_server_api", "web_server_api"),
    ("context_path", "context_path"),
    ("local_addr", "local_addr"),
    ("local_host", "local_host")
]
dotcompletions["cfhttp"] = [
    ("charSet", "charSet"),
    ("errorDetail", "errorDetail"),
    ("fileContent", "fileContent"),
    ("header", "header"),
    ("mimeType", "mimeType"),
    ("responseHeader", "responseHeader"),
    ("statusCode", "statusCode"),
    ("text", "text")
]
dotcompletions["server"] = [
    ("coldFusion.productName", "coldFusion.productName"),
    ("coldFusion.productVersion", "coldFusion.productVersion"),
    ("os.name", "os.name"),
    ("os.version", "os.version"),
    ("os.additionalInformation", "os.additionalInformation")
]
dotcompletions["cffile"] = [
    ("AttemptedServerFile", "AttemptedServerFile"),
    ("ClientDirectory", "ClientDirectory"),
    ("ClientFile", "ClientFile"),
    ("ClientFileExt", "ClientFileExt"),
    ("ClientFileName", "ClientFileName"),
    ("ContentSubType", "ContentSubType"),
    ("ContentType", "ContentType"),
    ("DateLastAccessed", "DateLastAccessed"),
    ("FileExisted", "FileExisted"),
    ("FileSize", "FileSize"),
    ("FileWasAppended", "FileWasAppended"),
    ("FileWasOverwritten", "FileWasOverwritten"),
    ("FileWasRenamed", "FileWasRenamed"),
    ("FileWasSaved", "FileWasSaved"),
    ("OldFileSize", "OldFileSize"),
    ("ServerDirectory", "ServerDirectory"),
    ("ServerFile", "ServerFile"),
    ("ServerFileExt", "ServerFileExt"),
    ("ServerFileName", "ServerFileName"),
    ("TimeCreated", "TimeCreated"),
    ("TimeLastModified", "TimeLastModified")
]


class DotCompletionsCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        sel = self.view.sel()[0]

        # insert the actual . character
        for region in self.view.sel():
            self.view.insert(edit, region.end(), ".")

        if not self.view.settings().get("auto_complete"):
            return

        word = self.view.word(sel.begin() - 1)
        word = self.view.substr(word).lower()
        if word in dotcompletions:
            completions.extend(dotcompletions[word])
            t = self.view.settings().get("auto_complete_delay")
            sublime.set_timeout(lambda:
                                self.view.run_command("auto_complete", {
                                    'disable_auto_insert': True,
                                    'next_completion_if_showing': False,
                                    'api_completions_only': True}), t)


class OnDotCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        _completions = []
        _completions.extend(completions)

        del completions[:]
        return _completions
