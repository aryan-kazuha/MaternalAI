import { useState } from "react";
import { MessageCircle, X } from "lucide-react";
import RagChat from "./RagChat";

export default function RagChatWidget() {
  const [open, setOpen] = useState(false);

  return (
    <>
      {/* Floating button */}
      <button
        type="button"
        onClick={() => setOpen(true)}
        className="fixed bottom-6 right-6 z-50 flex items-center justify-center w-14 h-14 rounded-full bg-[#2BB4A0] text-white shadow-xl hover:bg-[#259988]"
      >
        <MessageCircle className="w-7 h-7" />
      </button>

      {/* Slide‑up panel / modal */}
      {open && (
        <div className="fixed inset-0 z-50 flex items-end sm:items-center justify-center bg-black/20">
          <div className="w-full sm:max-w-xl mx-auto sm:rounded-2xl bg-transparent sm:bg-transparent">
            <div className="relative sm:mt-0 mt-auto">
              {/* Close button */}
              <button
                type="button"
                onClick={() => setOpen(false)}
                className="absolute -top-3 right-2 z-10 rounded-full bg-white shadow p-1 text-gray-600 hover:text-gray-900"
              >
                <X className="w-4 h-4" />
              </button>

              {/* Reuse your RagChat UI, but let it fill smaller height */}
              <div className="h-[70vh] sm:h-[520px]">
                <RagChat />
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  );
}
