import sublime, sublime_plugin, subprocess

class RsyncOnSave(sublime_plugin.EventListener):
	def on_post_save(self, view):

		filename = view.file_name()

		settings = sublime.load_settings('Rsync.sublime-settings')
		
		PROJECT_DIR = settings.get('rsync.project_dir')
		REMOTE_DIR = settings.get('rsync.remote_dir')

		if PROJECT_DIR in view.file_name():
			newfile = filename.replace(PROJECT_DIR, '')
			dirs = newfile.split('/')

			original_path = PROJECT_DIR + dirs[0]

			command = "rsync -au --exclude '.svn' --exclude '.hg' --exclude '.git' " + original_path + " " + REMOTE_DIR + " &"
			subprocess.call([command], shell = True)
