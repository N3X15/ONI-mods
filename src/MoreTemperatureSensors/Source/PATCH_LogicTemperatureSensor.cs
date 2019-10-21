using Harmony;

namespace MoreTemperatureSensors
{
    [HarmonyPatch(typeof(LogicTemperatureSensor))]
    [HarmonyPatch("UpdateLogicCircuit")]
    class PATCH_LogicTemperatureSensor_UpdateLogicCircuit
    {
        static bool Prefix(LogicTemperatureSensor __instance, bool ___switchedOn)
        {
            var lps = __instance.GetComponent<LogicPorts>();
            // UPSTREAM BUG (LU-341072): Nulls cause a crash in LogicPorts.SendSignal().
            if (lps.outputPorts != null)
            {
                lps.outputPorts.RemoveAll(item => item == null);
                lps.SendSignal(LogicSwitch.PORT_ID, (!___switchedOn) ? 0 : 1);
            }
            return false;
        }
    }
}
