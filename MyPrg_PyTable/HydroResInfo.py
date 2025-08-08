import copy
import math

const_FrameElementLeft = "    :....."
const_FrameElementRight = "....:     "
const_FrameElementVertical = "    :     "
const_FrameElementHorisontal = ".........."
const_FrameName = ".. Rs___.."
const_ConnectorCentral = "----|-----"
const_ConnectorLeft = "    |-----"
const_ConnectorRight = "----|     "
const_LineVertical = "    |     "
const_LineHorisontal = "----------"
const_LineFrameersection = "----:-----"
const_ResistanceElementar = "-[ Re___]-"
const_ResistanceLeftSide = "----:     "
const_ResistanceRightSide = "    :-----"
#
const_g_fall_acc = 9.81
#const_QParallelHydroResistancesMax = 16
const_LocResistanceGroupN = 1
const_WayResistanceGroupN = 2

class HydroSchemCanvas:
##{
     def __init__(self, dg=0):
    #{
        self.dg = dg
    #}
    

    def Draw_FrameElementLeft( x,  y):
    #{
        if (dg != null)
        #{
            self.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.FrameElementLeft
        #}
    #}
    def Draw_FrameElementRight( x,  y):
    #{
        if (dg != null)
        #{
            self.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.FrameElementRight
        #}
    #}
    def Draw_FrameElementVertical( x,  y):
    #{
        if (dg != null)
        #{
            self.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.FrameElementVertical
        #}
    #}
    def Draw_FrameElementHorisontal( x,  y)
    #{
        if (dg != null)
        #{
            self.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.FrameElementHorisontal
        #}
    #}
    def Draw_FrameName( x,  y,  N)
    #{
        string sn = N.ToString()
         L = sn.Length
        if (dg != null)
         #{
            self.dg.Rows[y - 1].Cells[x - 1].Value = "..[   R" + N.ToString() + "  ].."
            switch (L)
            #{
                case 1:
                    self.dg.Rows[y - 1].Cells[x - 1].Value = "..[  R" + sn + " ].."
                break
                case 2:
                    self.dg.Rows[y - 1].Cells[x - 1].Value = "..[ R" + sn + " ].."
                break
                case 3:
                    self.dg.Rows[y - 1].Cells[x - 1].Value = "..[ R" + sn + "].."
                    break
                case 4:
                    self.dg.Rows[y - 1].Cells[x - 1].Value = "..[R" + sn + "].."
                break
                default:
                    self.dg.Rows[y - 1].Cells[x - 1].Value = "..[R" + sn + "].."
                break
            #}
        #}
    #}
    def Draw_ConnectorCentral( x,  y)
    #{
        if (dg != null)
        #{
            self.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.ConnectorCentral
        #}
    #}
    def Draw_ConnectorLeft( x,  y)
    #{
        if (dg != null)
        #{
            self.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.ConnectorLeft
        #}
    #}
    def Draw_ConnectorRight( x,  y)
    #{
        if (dg != null)
        #{
            self.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.ConnectorRight
        #}
    #}
    def Draw_LineVertical( x,  y)
    #{
        if (dg != null)
        #{
            self.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.LineVertical
        #}
    #}
    def Draw_LineHorisontal( x,  y)
    #{
        if (dg != null)
        #{
            self.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.LineHorisontal
        #}
    #}
    def Draw_LineFrameersection( x,  y)
    #{
        if (dg != null)
        #{
            self.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.LineFrameersection
        #}
    #}
    def Draw_ResistanceElementar( x,  y,  N)
    #{
        string sn = N.ToString()
         L = sn.Length
        if (dg != null)
        #{
            self.dg.Rows[y - 1].Cells[x - 1].Value = "--[   R" + N.ToString() + "  ]--"
            switch (L)
            #{
                case 1:
                    self.dg.Rows[y - 1].Cells[x - 1].Value = "--[  R" + sn+ " ]--"
                break
                case 2:
                    self.dg.Rows[y - 1].Cells[x - 1].Value = "--[ R" + sn + " ]--"
                break
                case 3:
                    self.dg.Rows[y - 1].Cells[x - 1].Value = "--[ R" + sn + "]--"
                break
                case 4:
                    self.dg.Rows[y - 1].Cells[x - 1].Value = "--[R" + sn + "]--"
                break
                default:
                    self.dg.Rows[y - 1].Cells[x - 1].Value = "--[R" + sn + "]--"
                 break
            #}
        #}
    #}
    def Draw_ResistanceLeftSide( x,  y)
    #{
        if (dg != null)
        #{
            self.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.ResistanceLeftSide
        #}
    #}
    def Draw_ResistanceRightSide( x,  y)
    #{
        if (dg != null)
        #{
            self.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.ResistanceRightSide
        #}
    #}
    //
    def DrawEmptyCell( x,  y)
    #{
        if (dg != null)
        #{
            self.dg.Rows[y - 1].Cells[x - 1].Value = ""
        #}
    #}
    def SetSize( x,  y)
    #{
        if (dg != null)
        #{
            self.dg.RowCount = y
            self.dg.ColumnCount = x
        #}
        self.SetParams()
    #}
    def SetParams()
    #{
        if (dg != null)
        #{
            //for ( i = 1 i <= dg.RowCount i++)
            //#{
                for ( j = 1 j <= dg.ColumnCount j++)
                #{
                    self.dg.Columns[j - 1].Width = 86

                #}
            //#}//
            for ( i = 1 i <= dg.RowCount i++)
            #{
                self.dg.Rows[i - 1].Height = 20
            #}
        #}
    #}
    def Clear()
    #{
        for ( i = 1 i <= self.dg.RowCount i++)
        #{
            for ( j = 1 j <= self.dg.ColumnCount i++)
            #{
                DrawEmptyCell(i, j)
            #}
        #}
    #}
    def SetResistance( x,  y,  yUpper,  L,  H,  N,  QSubElts = 0)
    #{
         yLower = H - Math.Abs(yUpper)
        if (QSubElts == 0)
        #{
            self.Draw_ResistanceElementar(x, y, N)
        #}
        else
        #{
            self.Draw_LineFrameersection(x, y)
            self.Draw_FrameName(x + 1, y - Math.Abs(yUpper) + 1, N)
            self.Draw_FrameElementLeft(x, y - Math.Abs(yUpper) + 1)
            for ( i = 1 i <= Math.Abs(yUpper - 1) i++)
            #{
                self.Draw_FrameElementVertical(x, y - 1 + i)
                self.Draw_FrameElementVertical(x + L - 1, y - 1 + i)
            #}
            self.Draw_FrameElementRight(x + L - 1, y - Math.Abs(yUpper) + 1)
            self.Draw_FrameElementLeft(x, y + yLower - 1)
            for ( i = 1 i <= Math.Abs(yLower - 1) i++)
            #{
                self.Draw_FrameElementVertical(x, y - 1 + i)
                self.Draw_FrameElementVertical(x + L - 1, y - 1 + i)
            #}
            self.Draw_FrameElementRight(x + L - 1, y + yLower - 1)
            self.Draw_LineFrameersection(x + L - 1, y)
        #}
    #}//fn
#}//cl
