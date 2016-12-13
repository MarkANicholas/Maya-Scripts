import maya.cmds as cmds


#opens a window and closes one if it is already open
class TimelineWindow(object):

    winID = "TimelineClips"

    def show(self):
        if cmds.window(self.winID, query=True, exists=True):
            cmds.deleteUI(self.winID)

        window = cmds.window(self.winID, title=self.winID, iconName="Clips")
        cmds.columnLayout( adjustableColumn=True)
        cmds.button(w=600, label="Set Default Timeline", command=self.dtime)
        cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )
        cmds.setParent( '..' )
        cmds.showWindow( window )

    def dtime(self, *args):
        #set timeline to this
        time = {"rmin":0, "rmax":100, "start":0, "end":500}
        cmds.playbackOptions(min=time["rmin"], max=time["rmax"], animationStartTime=time["start"], animationEndTime=time["end"] )

